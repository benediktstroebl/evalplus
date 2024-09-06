
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
    if len(arr) <= 1:
        return 0

    front_half = arr[: len(arr) // 2]
    back_half = arr[len(arr) // 2 :][::-1]

    num_removed = 0
    for i in range(len(front_half)):
        if front_half[i] != back_half[i]:
            num_removed += 1

    return num_removed
