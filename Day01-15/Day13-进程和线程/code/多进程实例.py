
from multiprocessing import Process,Pool,Queue
import os,random
from time import sleep


# 子进程要执行的代码
def run_proc(name):
    for i in range(10):
        print('运行子进程 进程名：%s 进程标识：%s 进程ID：(%s)...' % (name,i, os.getpid()))
        sleep(random.random())






def main():
    print('主进程启动 主进程ID： %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    p1 = Process(target=run_proc, args=('test1',))
    print('子进程开始启动.')
    p.start()
    p1.start()
    p.join()
    p1.join()

    print('子进程结束.') #join阻塞p、p1执行结束后主进程继续执行


if __name__ == '__main__':
        main()
