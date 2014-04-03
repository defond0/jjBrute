import Queue
import random  
import time 

def randy(length):
    randy=[]
    for i in range(length):
            randy+=[random.randint(-1*length,length)]
    return randy

""" A simple merge sort using a iterative divide and conquer for O(nlogn) time"""
def mergeSort(list):
    """
    >>> mergeSort(['a','c','b','d'])
    ['a', 'b', 'c', 'd']
    >>> mergeSort([1,3,2,4,7,1,35,2])
    [1, 1, 2, 2, 3, 4, 7, 35]
    """
    q = Queue.Queue()
    size = len(list)
    n=0
    for i in range(size):
        q.put(list[i])
    while(q.qsize()!=1):
        if n<size:
            q.put(merge([q.get()],[q.get()]))
            n+=2
        else:
            q.put(merge(q.get(),q.get()))
    return q.get()
    
def merge(x=[],y=[]):
    """
    this takes in two sorted lists or sets, and returns their
    combination in a set
    >>> merge(['a','c'],['b','d'])
    ['a', 'b', 'c', 'd']
    >>> merge([1,3],[2,4])
    [1, 2, 3, 4]
    """
    if len(x)==0:
        return y
    if len(y)==0:
        return x
    if(x[0]<=y[0]):
        return  [x[0]]+merge(x[1:],y)
    else:
        return  [y[0]]+merge(x,y[1:]) 
        
def quickSort(list):
    """
    >>> quickSort(['a','c','b','d'])
    ['a', 'b', 'c', 'd']
    >>> quickSort([1,3,2,4,7,1,35,2])
    [1, 1, 2, 2, 3, 4, 7, 35]
    """
    s=len(list)
    if s<=1:
        return list
    pivotIdx=random.randint(0,s-1)
    pivot=list.pop(pivotIdx)
    left,right=[],[]
    for i in range(len(list)):
        if(list[i]<=pivot):
            left+=[list[i]]
        else:
            right+=[list[i]]
    return quickSort(left)+[pivot]+quickSort(right)

def radixIT(listy, mxlen, radix=10):
    """
    Iterative radix sort, 
#    >>> radixIT(['a','c','b','d'],1,10)
#    ['d', 'c', 'b', 'a']
    >>> radixIT([1,3,2,4,7,1,-35,2],2,10)
    [-35, 1, 1, 2, 2, 3, 4, 7]
    
    """
    poslist=[]
    neglist=[]
    for i in range(len(listy)):
        if listy[i]<0:
            neglist+=[listy[i]]
        else:
            poslist+=[listy[i]]
    for i in range(mxlen):
        negbuckets = [[]]*radix
        posbuckets = [[]]*radix
        for l in range(len(neglist)):
            idx=int(neglist[l])%radix
            negbuckets[idx]=negbuckets[idx]+[neglist[l]]
        for l in range(len(poslist)):
            idx=int(poslist[l])%radix
            posbuckets[idx]=posbuckets[idx]+[poslist[l]]
        negtemp=[]
        postemp=[]
        for k in range(len(negbuckets)):
            negtemp+=negbuckets[k]
        neglist=negtemp
        for k in range(len(posbuckets)):
            postemp+=posbuckets[k]
        poslist=postemp
        radix=radix*radix
    listy=neglist+poslist
    return listy 
    


def test():
    start=0 
    rr=10
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,2)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')
    
    start=0
    rr=100
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,3)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')
    
    start=0
    rr=1000
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,4)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')

    start=0
    rr=10000
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,5)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')
    

"""
TESTING SUITE 
"""


if __name__ == "__main__":
    
   
    import doctest
    doctest.ELLIPSIS
    doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=False)
    
    mr=999
    qr=999
    
    
    listmr=randy(mr)
    start = time.clock()
    listms=mergeSort(listmr) 
    totalm=(time.clock() - start) 
    listqr=randy(qr)
    start = time.clock()
    listqs=quickSort(listqr) 
    totalq=(time.clock() - start)
    
    print("Merge Sorting a Random List of "+str(mr)+" ints")
    print(str(totalm)+ 'seconds')
    print("Quick Sorting a Random List of "+str(qr)+" ints")
    print(str(totalq)+ 'seconds')
    start=0 
    rr=10
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,2)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')
    
    start=0
    rr=100
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,3)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')
    
    start=0
    rr=1000
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,4)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')

    start=0
    rr=10000
    listrr=randy(rr)
    start = time.clock()
    listrs=radixIT(listrr,5)
    totalr=(time.clock()-start)
    print("Radix Sorting a Random List of "+str(rr)+" ints")
    print(str(totalr)+ 'seconds')
    
#    rl=10 
#    maxdig=2
#    total=0
#    for i in range(3):
#        l=randy(rl)
#        total = 0
#        for i in range(3):
#              start = time.clock()
#              listrs=radixIT(l,maxdig)
#              total+=(time.clock()-start)
#        print("Radix list of len "+ str(rl)+ "--- "+ str(l))
#        print(listrs)
#        print(" with an average time ", total/3)
#        maxdig+=1
#        rl=rl*10
            
            
            
        
    
    
    
