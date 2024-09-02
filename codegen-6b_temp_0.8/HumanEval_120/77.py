
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
    def bin_search(arr, target, start, end):
        if start > end:
            return start - 1
        if start == end:
            if target > arr[start]:
                return start
            else:
                return start + 1
        mid = start + (end - start) // 2
        if target < arr[mid]:
            return bin_search(arr, target, start, mid - 1)
        elif target > arr[mid]:
            return bin_search(arr, target, mid + 1, end)
        else:
            return mid
    
    n = len(arr)
    result = []
    for i in range(n):
        pos = bin_search(arr, k, i + 1, n)
        if len(result) < k:
            if pos != i:
                result.append(arr[pos])
            elif pos < i:
                result.append(arr[pos])
    return result

arr = [-3, -4, 5, 5, 8, -4, 4, 5, 2, 1, 3, -5, -1, 3, -2, -4, -2, -3, -5, -4, -5, 5, -4, -3]
assert maximum(arr, 4) == [5, 5, 5, -3]
assert maximum(arr, 3) == [5, 5, 8]
assert maximum(arr, 2) == [5, 5]
assert maximum(arr, 1) == [5]
assert maximum(arr, 0) == [-3, -4, -3, -5]

arr = [-1, 1, -3, -5, 4, 4, -5, 3, 2, 1, -5, 4, 4, -6, -4, -4]
assert maximum(arr, 10) == [4, 4, 4, 3, 2, 1, -6, -5, -4, -3, -5, -4, -5, 4, 4]
assert maximum(arr, 9) == [4, 4, 4, 3, 2, 1, -6, -5, -4, -3, -5, -4, -5, 4, 4]
assert maximum(