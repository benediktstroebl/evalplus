
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
    # O(n) time and space
    if not arr:
        return 0
    mid = len(arr) // 2
    # first half of array
    first_half = arr[:mid]
    # reverse second half of array
    second_half = arr[mid:][::-1]
    # count of changes
    changes = 0
    for i in range(len(first_half)):
        if first_half[i] != second_half[i]:
            changes += 1
    return changes
