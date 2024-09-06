
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
    if not arr:
        return 0

    num_changes = 0

    # Loop through array and count the number of items that are not the same
    # at their respective opposite indices
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            num_changes += 1

    # If the length of the array is even, one of the middle two elements needs to
    # be changed to make the array palindromic.
    if len(arr) % 2 == 0:
        num_changes -= 1

    return num_changes
