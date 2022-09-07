from django.shortcuts import render
from django.http import HttpResponse
import random

def insertionsort(request):
    list = getList()
    return render(request, 'insertionsort.html', {'list': list})

def mergesort(request):
    list = getList()
    return render(request, 'mergesort.html', {'list': list}) 

def quicksort(request):
    global list
    list = getList()
    return render(request, 'quicksort.html', {'list': list}) 

def selectionsort(request):
    global list
    list = getList()
    return render(request, 'selectionsort.html', {'list': list})

def getList():
    return [random.randint(50, 500) for i in range(0, 50)]

def displayMergesort(request):
    animations = getMergeSortAnimation()
    return HttpResponse([animations])


def getMergeSortAnimation():
    list = getList()
    animations = []
    if len(list) <= 1: return list
    auxiliarylist = list.copy()
    mergeSortHelper(list, 0, len(list) - 1, auxiliarylist, animations)
    return animations


def mergeSortHelper(mainlist, start, end, auxiliarylist, animations):
    if start == end: return
    middle = (start + end) // 2
    mergeSortHelper(auxiliarylist, start, middle, mainlist, animations)
    mergeSortHelper(auxiliarylist, middle + 1, end, mainlist, animations)
    merge(mainlist, start, middle, end, auxiliarylist, animations)


def merge(mainlist, start, middle, end, auxiliarylist, animations):
    k = start
    i = start
    j = middle + 1
    while i <= middle and j <= end:
        animations.append([i, j])
        animations.append([i, j])
        if auxiliarylist[i] <= auxiliarylist[j]:
            animations.append([k, auxiliarylist[i]])
            mainlist[k] = auxiliarylist[i]
            k += 1
            i += 1
        else:
            animations.append([k, auxiliarylist[j]])
            mainlist[k] = auxiliarylist[j]
            k += 1
            j += 1

    while i <= middle:
        animations.append([i, i])
        animations.append([i, i])
        animations.append([k, auxiliarylist[i]])
        mainlist[k] = auxiliarylist[i]
        k += 1
        i += 1

    while j <= end:
        animations.append([j, j])
        animations.append([j, j])
        animations.append([k, auxiliarylist[j]])
        mainlist[k] = auxiliarylist[j]
        k += 1
        j += 1


def displayQuicksort(request):
    animations = getQuickSortAnimations(list)
    return HttpResponse([animations])


def getQuickSortAnimations(list):
    animations = []
    auxiliarylist = list.copy()
    quickSortHelper(auxiliarylist, 0, len(auxiliarylist) - 1, animations)
    return animations


def quickSortHelper(auxiliarylist, start, end, animations):
    if start < end:
        pivotIndex = partition(auxiliarylist, start, end, animations)
        quickSortHelper(auxiliarylist, start, pivotIndex - 1, animations)
        quickSortHelper(auxiliarylist, pivotIndex + 1, end, animations)


def partition(auxiliarylist, start, end, animations):
    pivot = auxiliarylist[end]
    pivotIndex = start
    for i in range(start, end):
        animations.append([i, end])
        animations.append([i, end])
        if auxiliarylist[i] <= pivot:
            animations.append([i, auxiliarylist[pivotIndex]])
            animations.append([pivotIndex, auxiliarylist[i]])
            auxiliarylist[i], auxiliarylist[pivotIndex] = auxiliarylist[pivotIndex], auxiliarylist[i]
            pivotIndex += 1
        else:
            animations.append([-1, -1])
            animations.append([-1, -1])
        animations.append([-1, -1])
        animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([-1, -1])
    animations.append([pivotIndex, auxiliarylist[end]])
    animations.append([end, auxiliarylist[pivotIndex]])
    auxiliarylist[pivotIndex], auxiliarylist[end] = auxiliarylist[end], auxiliarylist[pivotIndex]
    return pivotIndex


def displaySelectionsort(request):
    animations = getSelectionSortAnimations(list)
    return HttpResponse([animations])


def getSelectionSortAnimations(list):
    animations = []
    auxiliarylist = list.copy()
    selectionSortHelper(auxiliarylist, animations)
    return animations


def selectionSortHelper(auxiliarylist, animations):
    for i in range(0, len(auxiliarylist)):
        minIndex = i
        for j in range(i+1, len(auxiliarylist)):
            animations.append([999, j, minIndex])
            animations.append([9999, j, minIndex])
            if auxiliarylist[j] < auxiliarylist[minIndex]:
                minIndex = j
        animations.append([99999, minIndex, auxiliarylist[i]])
        animations.append([99999, i, auxiliarylist[minIndex]])

        auxiliarylist[minIndex], auxiliarylist[i] = auxiliarylist[i], auxiliarylist[minIndex]


def displayInsertionsort(request):
    list = getList()
    animations = getInsertionSortAnimations(list)
    return HttpResponse([animations])


def getInsertionSortAnimations(list):
    animations = []
    auxiliarylist = list.copy()
    selectionSortHelper(auxiliarylist, animations)
    return animations


def insertionSortHelper(auxiliarylist, animations):
    for i in range(1, len(auxiliarylist)):
        key = auxiliarylist[i]
        j = i - 1
        animations.append([999, j, i])
        animations.append([9999, j, i])
        while j >= 0 and auxiliarylist[j]>key:
            animations.append([99999, j + 1, auxiliarylist[j]])
            auxiliarylist[j + 1] = auxiliarylist[j]
            j -= 1
            if j >= 0:
                animations.append([999, j, i])
                animations.append([9999, j, i])
        animations.append([99999, j + 1, key])
        auxiliarylist[j + 1] = key