
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

    if len(arr) < 2:
        return 0

    end = len(arr) - 1
    front_to_end_changes = 0
    end_to_front_changes = 0
    for i in range(0, len(arr) // 2):
        if arr[i] != arr[end - i]:
            front_to_end_changes += 1
    if len(arr) % 2 == 1:
        if arr[len(arr) // 2] != arr[len(arr) // 2 + 1]:
            end_to_front_changes += 1
    return min(front_to_end_changes, end_to_front_changes)

