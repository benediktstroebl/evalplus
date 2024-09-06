
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
    result = []
    for num in arr:
        if len(result) < k:
            if len(result) == 0 or num > result[-1]:
                result.append(num)
            else:
                break
    return result


assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
assert maximum([4, -4, 4], 2) == [4, 4]
assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2]
assert maximum([-3, -4, -1, -5], 1) == [-4]
assert maximum([-4], 1) == [-4]
assert maximum([-3, 0], 2) == [-3, 0]
assert maximum([], 2) == []
assert maximum([3, 2, 3, 2, 3, ], 1) == [3]
assert maximum([2, 3, -4, 1, -2], 2) == [2, 3]
assert maximum([1, -3, 5, -2, 6, 7, -1, -2], 3) == [-1, -2, -3, 5, 6, 7]
assert maximum([2, -3, 5, 6, -7, 8, 9, 1, -2, 3, 4, -5, -6], 4) == [-5, -6, -7, -2, 3, 4, 5, 6, 8, 9]
assert maximum([2, -3, 5, 6, -7, 8, 9, 1, -2, 3, 4, -5, -6], 1) == [-2]
assert maximum([2, -3, 5, 6, -7, 8, 9, 1, -2, 3, 4, -5, -6], 5) == [-3, -2, 1, 2, 3, 4, 5]
assert maximum([2, -3, 5, 6, -7, 8, 9, 1, -2, 3, 4, -5, -6], 9) == [-5, -6, -7, -2, 3, 4, 5, 6, 8, 9]

