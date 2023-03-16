# python3
import fileinput
import sys
import threading

def build_min_heap(data, i, swaps):
    left = 2 * i + 1
    right = 2 * 1 + 2

    if left < len(data) and data[left] < data[i]:
        smallest = left
    else:
        smallest = i

    if right < len(data) and data[right] < data[smallest]:
        smallest = right

    if smallest != i:
        swaps.append([i, smallest]) 
        data[i], data[smallest] = data[smallest], data[i]
        build_min_heap(data, smallest, swaps)

def build_heap(data):
    swaps = []

    for i in range(int((len(data)//2)-1), -1, -1):
        build_min_heap(data, i, swaps)

    return swaps


def main():

    data= []

    ievade = input()
    text = ""
    if ievade == "F":
        text = input() 
        with open(text) as f: 
            lines = f.readlines()
            n = int(lines[0])
            array = lines[1].split()
            for a in array:
                data.append(int(a))
    if ievade == "I":
        n = int(input())
        data = list(map(int, input().split()))

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()