
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

    # solution 1, brute force
    """
    arr = [-3, -4, 5]
    k = 3
    res = []
    for i in range(len(arr)):
        if len(res) < k:
            res.append(arr[i])
        else:
            if arr[i] > res[len(res)-1]:
                res.pop()
                res.append(arr[i])
    print(res)
    """
    # solution 2, PriorityQueue
    """
    import heapq
    arr = [-3, -4, 5]
    k = 3
    heap = []
    for i in range(len(arr)):
        if len(heap) < k:
            heapq.heappush(heap, -arr[i])
        else:
            if arr[i] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -arr[i])

    res = [x for x in heapq.nsmallest
