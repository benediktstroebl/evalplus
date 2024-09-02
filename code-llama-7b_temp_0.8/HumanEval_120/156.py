
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # def maxHeapify(arr, i, heapSize):
    #     largest = i
    #     l = 2*i + 1
    #     r = 2*i + 2

    #     if l < heapSize and arr[i] < arr[l]:
    #         largest = l
        
    #     if r < heapSize and arr[largest] < arr[r]:
    #         largest = r
        
    #     if largest != i:
    #         arr[i], arr[largest] = arr[largest], arr[i]
    #         maxHeapify(arr, largest, heapSize)

    # def buildMaxHeap(arr, heapSize):
    #     for i in range(heapSize//2, 0, -1):
    #         maxHeapify(arr, i, heapSize)

    # def heapSort(arr, heapSize):
    #     for i in range(len(arr), 0, -1):
    #         arr[0], arr[i-1] = arr[i-1], arr[0]
    #         heapSize -= 1
    #         maxHeapify(arr, 0, heapSize)

    #     return arr

    # heapSize = len(arr)
    # buildMaxHeap(arr, heapSize)
    # return heapSort(arr, heapSize)[0:k]

    heap = list()
    for i in range(k):
        heapq.heappush(heap, -arr[i])

    for i in range(k, len(arr)):
        if heap[0] < arr[i]:
            heapq.heappop(heap)
            heapq.heappush(heap, -arr[i])
    
    return [-heap[0]] * k

