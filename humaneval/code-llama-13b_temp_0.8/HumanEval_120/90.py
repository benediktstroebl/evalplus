
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
    heap = []
    # use negative number to get min heap
    for i, n in enumerate(arr):
        if i < k:
            heapq.heappush(heap, (n, i))
        else:
            # if the new number is larger than the last one, replace it
            if heap[0][0] < n:
                heapq.heappop(heap)
                heapq.heappush(heap, (n, i))
    return [x[0] for x in heap]

