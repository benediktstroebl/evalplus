
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
    differences = 0
    for i in range(1, len(arr)):
        differences += 1
        if arr[i] != arr[len(arr) - i - 1]:
            differences += 1
    return differences


assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 4, 3, 2, 5]) == 1
assert smallest_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]) == 2
