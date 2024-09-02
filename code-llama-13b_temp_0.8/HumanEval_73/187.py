
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
    if len(arr) <= 2:
        return 0
    half = len(arr)//2
    before = arr[:half]
    after = arr[half:]
    # check if even number of elements
    if len(arr) % 2 != 0:
        after = after[1:]
    return sum(before) - sum(after)

