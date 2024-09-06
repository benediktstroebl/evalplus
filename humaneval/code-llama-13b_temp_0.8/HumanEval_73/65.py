
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    # A = O(n) space
    if not arr:
        return 0
    even = 0
    odd = 0
    for i in arr:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == len(arr) or odd == len(arr):
        return 0
    return min(even, odd)
