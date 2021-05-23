import datetime
from numpy import random
import sys
sys.setrecursionlimit(55000)

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


A=random.randint(100, size=(20000))
B=A.copy()
C=A.copy()
print("Bubble_sort,random", calculateExecutionTime(A, bubbleSort))
print("Heap_sort,random", calculateExecutionTime(B, heapSort))
print("Quick_sort,random", calculateExecutionTime(C, quickSort))

A=random.randint(100, size=(20000))
A.sort()
B=A.copy()
C=A.copy()

print("Bubble_sort,sorted", calculateExecutionTime(A,bubbleSort))
print("Heap_sort,sorted", calculateExecutionTime(B,heapSort))
print("Quick_sort,sorted", calculateExecutionTime(C,quickSort))

A=random.randint(100, size=(20000))
A.sort()
B=A.copy()
C=A.copy()

print("Bubble_sort,reverse_sorted", calculateExecutionTime(A[::-1], bubbleSort))
print("Heap_sort,reverse_sorted", calculateExecutionTime(B[::-1], heapSort))
print("Quick_sort,reverse_sorted", calculateExecutionTime(C[::-1], quickSort))

# Próbka danych: 200000 rekordów.
# Dla wszystkich typów tablic, najszybszym algorytmem sortującym okazał się heap sort.
# Quick sort jedynie w przypadku tablic losowych jest w stanie dorównać heap_sort pod względem czasu wykonania. W tablicach posortowanych oraz odwrotnie posortowanych jest zauważalnie wolniejszy.
# Sortowanie bąbelkowe jest wielokrotnie mniej wydajnym algorytmem od pozostałych dwóch, i nie powinno być używane dla jakichkolwiek większych zbiorów danych.