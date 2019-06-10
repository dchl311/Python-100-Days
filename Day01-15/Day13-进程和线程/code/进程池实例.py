'''
进程池
pool 
pool=Pool(3)#表示进程池最多有3个进程一起执行
pool.apply_async(workr,(i,))#向进程池中添加任务
如果添加的任务数量超过了进程池中进程的个数的话，也不会导致添加不进去
添加到进程中的任务，如果还没有被执行的话，那么此时他们会等待进程池中的
经常完成一个任务后，会自动的去用刚刚的那个进程，完成当前的新任务
pool.close()关闭进程池，相当于不能够再次添加新任务了
pool.join()主进程 创建/添加 任务后，默认不会等待进程池中的任务执行完后才结束，
而是主进程的任务结束后，立马结束，如果没有join（）,会导致进程池的任务不会执行

等待pool中所有的子进程执行完毕

这种方式下：一般主进程用来等待，真正的任务都是在子进程中完成

非堵塞式添加进程到进程池：

'''

from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()  # 记录从1970.0.0到现在的秒数
    print("%s 开始执行，进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))

def main():
    po = Pool(6)  # 定义一个进程池，最大进程数3
    for i in range(0, 10):
        po.apply_async(worker, (i,))
    print("---start---")
    po.close()  # 关闭进程池，关闭后po不再接受新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close后
    print("-----------end----------")
def test():
    po = Pool(6)  # 定义一个进程池，最大进程数3
    for i in range(0, 10):
        po.apply(worker, (i,))
    print("---start---")
    po.close()  # 关闭进程池，关闭后po不再接受新的请求
    #po.join()  # 等待po中所有子进程执行完成，必须放在close后
    print("-----------end----------")



if __name__ == "__main__":
    test()


