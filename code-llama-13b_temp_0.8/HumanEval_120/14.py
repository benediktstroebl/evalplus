
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
    ## Solution 1
    # res = sorted(arr)
    # return res[-k:]

    ## Solution 2
    # res = sorted(arr)[:k]
    # return res[::-1]

    ## Solution 3
    heapq.heapify(arr)
    res = []
    while k:
        res.append(heapq.heappop(arr))
        k -= 1
    return res[::-1]

