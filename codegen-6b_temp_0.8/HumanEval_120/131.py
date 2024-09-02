
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
    if not arr or k == 0:
        return []

    # max_heap
    heap, res = [-arr[0]], []
    for num in arr[1:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)
        else:
            heapq.heappush(heap, num)

    res.append(heapq.heappop(heap))
    for _ in range(k - 1):
        if res[-1] > heap[0]:
            heapq.heappushpop(heap, res[-1])
        res.append(heapq.heappop(heap))
    return [-x for x in res]
