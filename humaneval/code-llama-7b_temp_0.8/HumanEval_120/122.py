
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
    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    n = len(arr)
    if k == n:
        return sorted(arr)
    elif k >= n:
        return arr

    return sorted(arr, reverse=True)[n-k:]


    # Time Complexity: O(nlogk)
    # Space Complexity: O(k)
    n = len(arr)
    if k == n:
        return sorted(arr)
    elif k >= n:
        return arr

    res = []
    for i in range(k):
        cur_max = float('-inf')
        for j in range(i, n):
            cur_max = max(cur_max, arr[j])
        res.append(cur_max)

    return res
