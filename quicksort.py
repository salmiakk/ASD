import datetime

def quickSort(A,p,r):
    if (p < r):
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

def partition(A,p,r):
    pivot = A[r]
    smaller = p
    # range() stops before the second argument
    for j in range(p, r):
        if(A[j] <= pivot):
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller
def build_max_heap(a):
    heapSize = len(a) - 1
    for i in range(int(len(a)*0.5), -1, -1):
        max_heapify(a,i,heapSize)
        
def max_heapify(a, i, heapSize):
    l=2*i+1
    r=2*i+2
    if(l <= heapSize and a[l] > a[i]):
        largest = l
    else:
        largest = i
    if( r <= heapSize and a[r] > a[largest]):
        largest = r
    if i is not largest:
        a[largest], a[i] = a[i], a[largest]
        max_heapify(a, largest,heapSize)
def heapSort(a):
    build_max_heap(a)
    heapSize = len(a) - 1
    for i in range(heapSize, -1, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, 0, i-1)

def bubbleSort(a):
    n = len(a)
    while(n > 1):
        for i in range(n-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        n = n-1

def calculateExecutionTime(a, f):
    if f is quickSort:
        now = datetime.datetime.now()
        f(a,0,len(a)-1)
        end = datetime.datetime.now()
    else:
        now = datetime.datetime.now()
        f(a)
        end = datetime.datetime.now()
    return end-now


# 50 elements in each array

A = [7,10,20,15,4,3,3,8,100,1,7,10,20,15,4,3,3,8,100,1,7,10,20,15,4,3,3,8,100,1,7,10,20,15,4,3,3,8,100,1,7,10,20,15,4,3,3,8,100,1]
print("Bubble_sort,random", calculateExecutionTime(A, bubbleSort))
print("Heap_sort,random", calculateExecutionTime(A, heapSort))
print("Quick_sort,random", calculateExecutionTime(A, bubbleSort))

B = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
print("Bubble_sort,sorted", calculateExecutionTime(B,bubbleSort))
print("Heap_sort,sorted", calculateExecutionTime(B,heapSort))
print("Quick_sort,sorted", calculateExecutionTime(B,bubbleSort))

C = [50,49,48,47,46,45,44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
print("Bubble_sort,reverse_sorted", calculateExecutionTime(C, bubbleSort))
print("Heap_sort,reverse_sorted", calculateExecutionTime(C, heapSort))
print("Quick_sort,reverse_sorted", calculateExecutionTime(C, bubbleSort))


# Dla danych posortowanych, najlepiej sprawdza się sortowanie bąbelkowe (w tym algorytmie złożoność przy takim zbiorze danych wynosi O(n)).
# W przypadku danych losowych, algorytmy heap_sort oraz quick_sort wykazały bardzo podobny czas wykonania - w obu przypadkach złożoność wynosi O(nlogn).
# Dla danych odwrotnie posortowanych wyraźnie zauważamy bardzo niską wydajność sortowania bąbelkowego. Algorytmy heap_sort i quick_sort wykazują w tym przypadku podobne czasy wykonania.