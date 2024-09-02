
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
    # Special case when array is empty, we cannot do anything
    if len(arr) == 0:
        return 0

    # Build lookup table to store the number of changes for each index
    changes = [0] * len(arr)

    # Iterate backwards and forwards to compute changes
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                changes[i] += 1

    return min(changes)

