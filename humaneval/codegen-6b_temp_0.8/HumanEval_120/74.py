
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
    return list(sorted(arr, reverse = True)[:k])

assert [4, 4] == maximum([4, -4, 4], 2)
assert [-4, -3, 5] == maximum([-3, -4, 5], 3)
assert [4] == maximum([-3, 2, 1, 2, -1, -2, 1], 1)
assert [4, 4] == maximum([-3, 2, 1, 2, -1, -2, 1], 2)
assert [1] == maximum([1, -5, 5, -4, 4, 3, -2], 1)
assert [5, 4] == maximum([-3, 2, 1, 2, -1, -2, 1], 2)
assert [-4, -3, 5] == maximum([-3, -4, 5], 3)
assert [-4, -3, 5] == maximum([-3, -4, 5], 4)
assert [-4, -3, 5] == maximum([-3, -4, 5], 5)
assert [-4, -3, 5] == maximum([-3, -4, 5], 6)
assert [-4, -3, 5] == maximum([-3, -4, 5], 7)
assert [5] == maximum([-3, -4, 5], 8)
assert [5, 4] == maximum([-3, -4, 5], 9)
assert [5] == maximum([-3, -4, 5], 10)
assert [5, 4] == maximum([-3, -4, 5], 11)
assert [5, 4] == maximum([-3, -4, 5], 12)

