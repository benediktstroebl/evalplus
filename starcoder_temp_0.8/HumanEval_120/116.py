
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
    # if k >= len(arr):
    #     return arr

    # arr.sort()
    # return arr[-k:]

    # heapq.heapify(arr)
    # return [heapq.heappop(arr) for _ in range(k)]

    # min_heap = []
    # for i in arr:
    #     if len(min_heap) == k:
    #         if i > min_heap[0]:
    #             heapq.heappop(min_heap)
    #             heapq.heappush(min_heap, i)
    #     else:
    #         heapq.heappush(min_heap, i)

    # return min_heap

    from heapq import heappush, heappop

    min_heap = []
    for i in arr:
        if len(min_heap) < k:
            heappush(min_heap, i)
        elif i > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, i)

    return sorted(min_heap, reverse=True)

