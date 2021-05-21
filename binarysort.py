# Złożność algorytmu wynosi O(n)
def binarySort(A):
    # szukamy liczby mniejszej oraz większej
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            bigger = A[i+1]
            smaller = A[i]
    # sortujemy
    j = 0
    for i in range(len(A)):
        if A[i] < bigger:
            A[i], A[j] = A[j], A[i]
            j = j+1



A = [3,3,3,3,4,3,3,4,4,4,4,3,3,3,3,4]
binarySort(A)
print(A)