
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
    # if len(arr) == 1:
    #     return 0
    # if len(arr) % 2 != 0:
    #     return 1
    # if len(arr) == 2:
    #     return 0 if arr[0] != arr[1] else 1
    # if len(arr) == 3:
    #     return 2 if arr[1] < arr[0] < arr[2] else 3
    # mid = len(arr) // 2
    # if arr[mid - 1] < arr[mid] < arr[mid + 1] and arr[mid - 1] < arr[mid + 1] < arr[mid]:
    #     return 0
    # return 1 + smallest_change([-1 * i for i in arr])

    arr.sort()

    max_diff = max(arr[i] - arr[i - 1] for i in range(1, len(arr)))

    for i in range(len(arr) // 2):
        max_diff = min(max_diff, arr[i + 1] - arr[i])

    return max_diff


assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 4, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([5, 4, 7, 9, 6]) == 4
assert smallest_change([1, 2, 3, 4, 3]) == 1
assert smallest_change([-1, -2, -3, -4, -3, -2, -2]) == 1
assert smallest_change([-1, 0, 1, 2, 3, 4, 5, -3]) == 4
assert smallest_change([-1, -2, -3, -4, -1, -2]) == 2
assert smallest_change([-1, -2, -3, -4, -3, -2, -2]) == 1

import pytest

pytest.main(__file__)