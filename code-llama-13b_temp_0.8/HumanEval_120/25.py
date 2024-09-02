
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
    if len(arr) == k:
        return arr
    else:
        length = len(arr)
        arr = arr[:k]
        k = k % length
        if k:
            i = k
            j = k + k
            while i < length:
                if arr[j] > arr[k]:
                    arr[j], arr[k] = arr[k], arr[j]
                k += 1
                i += 1
                if k == length:
                    k = 0
                if j == length:
                    j = 0
        return arr

