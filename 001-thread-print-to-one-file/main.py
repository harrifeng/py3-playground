import threading


class MyThread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        for i in range(1000):
            print("starting thread :" + str(self.thread_id))


if __name__ == '__main__':
    threads = []
    for i in range(100):
        t = MyThread(i)
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
