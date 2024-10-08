
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
    arr_length = len(arr)

    if arr_length % 2 == 0:
        arr_mid_point = arr_length / 2
        start = 0
        end = arr_mid_point
    else:
        arr_mid_point = arr_length / 2 + 1
        start = 0
        end = arr_mid_point - 1

    while start < arr_mid_point and end < arr_length:
        if arr[start] != arr[end]:
            return arr_length - 2
        start += 1
        end += 1

    return 0

