
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
    n = len(arr)
    if n <= k:
        return sorted(arr)

    min_q, max_q = [], []

    for i in range(k):
        if len(min_q) == 0:
            heapq.heappush(min_q, arr[i])
        elif len(max_q) == 0:
            heapq.heappush(max_q, -arr[i])
        elif arr[i] < -min_q[0]:
            heapq.heapreplace(min_q, arr[i])
        elif arr[i] > -max_q[0]:
            heapq.heapreplace(max_q, -arr[i])

    if len(max_q) < len(min_q):
        heapq.heapify(max_q)
        return [-q for q in max_q]
    else:
        heapq.heapify(min_q)
        return min_q

