# coding=utf-8
import os
import judger

base_path = os.path.dirname(os.path.abspath(__file__))


def _compile():
    return judger.run(path="/usr/bin/gcc",
                      in_file=os.path.join(base_path, "in"),
                      out_file=os.path.join(base_path, "gcc_out"),
                      max_cpu_time=2000,
                      max_memory=200000000,
                      args=[os.path.join(base_path, "demo.c"), "-o", os.path.join(base_path, "demo")],
                      env=["PATH=" + os.environ["PATH"]],
                      use_sandbox=False)


def run(use_sandbox):
    _compile()
    path = os.path.join(base_path, "demo")
    return judger.run(path=path,
                      in_file=os.path.join(base_path, "in"),
                      out_file=os.path.join(base_path, "out"),
                      # ms
                      max_cpu_time=2000,
                      # Byte
                      max_memory=200000000,
                      # args and env are optional
                      args=["1", "2", "####"],
                      env=["aaa=123"],
                      # default is True
                      use_sandbox=use_sandbox)


print "With sandbox"
print run(use_sandbox=True)
print 'Without sandbox'
print run(use_sandbox=False)
