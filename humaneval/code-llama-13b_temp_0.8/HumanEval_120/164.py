
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

    # # Method 1: using heapq
    # import heapq

    # if k > len(arr):
    #     return sorted(arr, reverse=True)

    # heap = arr[: k]
    # heapq.heapify(heap)

    # for i in range(k, len(arr)):
    #     if heap[0] < arr[i]:
    #         heapq.heapreplace(heap, arr[i])

    # return heap

    # # Method 2: using heapq (optimized)
    # import heapq

    # if k > len(arr):
    #     return sorted(arr, reverse=True)

    # heap = arr[: k]
    # heapq.heapify(heap)
    # # Then we replace with arr[i] < heap[0].
    # # Since we use heap[0] as the comparison for next i, and 
    # # heap[0] is always the minimum, so we can just replace heap[0] 
    # # with arr[i] if arr[i] < heap[0].
    # for i in range(k, len(arr)):
    #     if arr[i] < heap[0]:
    #         heapq.heapreplace(heap, arr[i])

    # return heap

    # Method 3: using heapq (optimized)
    import heapq

    if k > len(arr):
        return sorted(arr, reverse=True)

    heap = arr[: k]
    heapq.heapify(heap)
    # Then we replace with arr[i] < heap[0].
    # Since we use heap[0] as the comparison for next i, and 
    # heap[0] is always the minimum, so we can just replace heap[0] 
    # with arr[i] if arr[i] < heap[0].
    for i in range(k, len(arr)):
        if arr[i] < heap[0]:
            heapq.heapreplace(heap, arr[i])

    return heap

