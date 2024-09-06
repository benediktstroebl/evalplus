
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
    start = 0
    end = len(arr) - 1
    for i in range(len(arr)):
        if arr[i] > arr[start]:
            start = i
    for i in range(start + 1, len(arr)):
        if arr[i] > arr[end]:
            end = i
    ans = [arr[i] for i in range(start, end + 1)]
    ans.sort()
    ans = ans[:k]
    return ans

