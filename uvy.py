import queue

pqueue=queue.PriorityQueue()
pqueue.put((12,"A"))
pqueue.put((6,"B"))
pqueue.put((3,"D"))
pqueue.put((3,"C"))

while queue:
    print(pqueue.get())
    pqueue.empty()