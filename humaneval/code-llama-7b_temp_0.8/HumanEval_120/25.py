
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
    if not arr or not k: return None

    # k elements
    n = len(arr)
    if k == n: return sorted(arr)

    # max k elements
    res = [None] * k
    for i in range(k):
        max_idx = -1
        for j in range(i, n):
            if res[i] == arr[j] or res[i] is None:
                continue
            if res[max_idx] is None or res[max_idx] < arr[j]:
                max_idx = j
        res[max_idx] = arr[max_idx]
    return res

