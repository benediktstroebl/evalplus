
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
    if len(arr) == 0:
        return 0
    # If the array is even, one change will make it a palindrome
    if len(arr) % 2 == 0:
        return 1
    # The min number of changes is the same as the left half transforming to the
    # right and the right half transforming to the left if the value is the same
    # and if the value is the same, it's not changed (if it's the same, it's still 1)
    return min(smallest_change(arr[:len(arr) // 2]), smallest_change(arr[len(arr) // 2:]))

