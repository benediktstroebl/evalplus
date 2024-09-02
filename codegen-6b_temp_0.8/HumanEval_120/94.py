
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
    if not arr:
        return []
    maximum = -float('inf')
    for elem in arr:
        maximum = max(elem, maximum)
    return sorted(arr, key=lambda x: -maximum)[:k]


assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
assert maximum([0], 1) == [0]
assert maximum([2, 3], 2) == [2, 3]
assert maximum([1, 2, 3, 4], 3) == [4, 3, 2]
assert maximum([-3, -4, 5], 3) == [-4, -3, 5]
assert maximum([-3, 2, 1, 2, -1, -2, -1], 1) == [2]
assert maximum([-4, 4], 1) == [-4, 4]
assert maximum([-3, 2, 1, 2, -1, -2, -1], 2) == [-2, -1]
assert maximum([-4, 4], 0) == []
assert maximum([-4, 4], 2) == [-4, 4]
assert maximum(list(range(100)), 50) == list(range(50, 100))
assert maximum(list(range(100)), 0) == []
assert maximum(list(range(100)), -2) == []
assert maximum([2, 1, 2, 10, -10, -1], 3) == [2, 2, 2, 10, -10, -1]
assert maximum([2, 1, 2, 10, -10, -1], -1) == [2, 1, 2, 10, -10, -1]
assert maximum([2, 1, 2, 10, -10, -1], 0) == [2, 1, 2, 10, -10, -1]
assert maximum([2, 1, 2, 10, -10, -1], 2) == [2, 1, 2, 10, -1]
assert maximum([2, 1, 2, 10, -10, -1], 1) == [2]
assert maximum([2, 1, 2, 10, -10, -1], 4) == [2, 1, 2, 10, -1]
assert maximum([2