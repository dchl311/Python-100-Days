from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    s='bfkjlsjklhfj'
    for value in s:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(1)

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    t_start = time.time()
    # 父进程创建Queue，并传给各个子进程：
    q = Queue(3)
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    t_stop = time.time()
    print( "执行完毕，耗时%0.2f" % (t_stop - t_start))