
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
    if k > n:
        return []
    left, right = 1, n+1
    while left < right:
        while arr[left] < 0:
            left += 1
        while arr[right] < 0:
            right -= 1
        mid = (left + right) // 2
        if arr[mid] > 0:
            left, right = mid, n+1
        elif arr[mid] < k:
            right = mid
        else:
            return []
    return arr[left:right]