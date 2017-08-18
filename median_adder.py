#!/usr/bin/env python
from sys import argv
from heapq import heappush, heappop

def parse(inputText):
    with open(inputText, "r") as f:
        tempList = [elem for elem in f.read().split('\n')][:-1]
        return ([int(elem) for elem in tempList])

def get_medians(stream):
    minHeap = []
    maxHeap = []
    medians = []
    effective_middle = 0
    for num in stream:
        if len(minHeap) > len(maxHeap):
            if num < effective_middle:
                heappush(maxHeap, -1 * heappop(minHeap))
                heappush(minHeap, -1 * num)
            else:
                heappush(maxHeap, num)
            medians.append(-1 * minHeap[0]) # even number of elements, so i/2th element
            effective_middle = ((-1 * minHeap[0]) + maxHeap[0]) / 2
        elif len(minHeap) < len(maxHeap):
            if num < effective_middle:
                heappush(minHeap, -1 * num)
            else:
                heappush(minHeap, -1 * heappop(maxHeap))
                heappush(maxHeap, num)
            medians.append(-1 * minHeap[0]) # even number of elements, so i/2th element
            effective_middle = ((-1 * minHeap[0]) + maxHeap[0]) / 2
        else:
            if num < effective_middle:
                heappush(minHeap, -1 * num)
                medians.append(-1 * minHeap[0]) # odd number of elements and more in minHeap
                effective_middle = -1 * minHeap[0]
            else:
                heappush(maxHeap, num)
                medians.append(maxHeap[0]) # odd number of elements and more in maxHeap
                effective_middle = maxHeap[0]
    return medians

if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: ./median_adder.py numbers.txt")
        exit()
    stream = parse(argv[1])
    medians = get_medians(stream)
    #print("Medians: " + str(medians))
    print("Last four digits of sum of medians: " +  str(sum(medians) % 10000))
