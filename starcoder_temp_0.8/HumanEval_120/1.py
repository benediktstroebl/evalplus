
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

    if k == 1:
        return [max(arr)]

    n = len(arr)
    result = [-1] * k
    for i in range(k):
        result[i] = arr[0]

    for i in range(1, n):
        if arr[i] > result[-1]:
            result[-1] = arr[i]
        else:
            result[k - 1] = arr[i]
            j = k - 2
            while j >= 0 and arr[i] > result[j]:
                result[j + 1] = result[j]
                j -= 1
            result[j + 1] = arr[i]

    return result

