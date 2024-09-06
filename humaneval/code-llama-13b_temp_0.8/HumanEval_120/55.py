
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
    # min_heap = []
    # max_heap = []
    # for i in range(k):
    #     if len(min_heap) == k:
    #         heapq.heappush(min_heap, arr[i])
    #     else:
    #         heapq.heappush(max_heap, -arr[i])
    #     while len(min_heap) > k:
    #         heapq.heappush(max_heap, -heapq.heappop(min_heap))
    #     while len(max_heap) > 0 and -max_heap[0] <= min_heap[0]:
    #         heapq.heappush(min_heap, -heapq.heappop(max_heap))
    # return [-i for i in min_heap]
    from heapq import heappushpop, heappush, heapreplace, nlargest
    heap = []
    for i in range(k):
        heappush(heap, -arr[i])
    for i in range(k, len(arr)):
        if -arr[i] > heap[0]:
            heappushpop(heap, -arr[i])
    return [-i for i in heap]

