
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
    num_of_changes = 0
    arr_len = len(arr)

    for i in range(arr_len // 2):
        if arr[i] != arr[arr_len - 1 - i]:
            num_of_changes += 1

    if num_of_changes == 0:
        return 0
    else:
        return num_of_changes