
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
    # We want to change the smallest amount of elements in the array
    # since we know that we can always get a palindrome, we can check
    # every possible palindrome and return the smallest number of changes
    # possible
    min_changes = len(arr)

    for i in range(0, len(arr) // 2):
        # We are not allowed to change the first and last elements
        if i != 0 and i != len(arr) - 1:
            # We change arr[i] to arr[len(arr) - 2 - i]
            # and arr[len(arr) - 1 - i]
            # Note: len(arr) - 1 - i is the length of the array backwards
            min_changes = min(min_changes, 2 + smallest_change(arr[i + 1:len(arr) - 1 - i]))

    return min_changes

