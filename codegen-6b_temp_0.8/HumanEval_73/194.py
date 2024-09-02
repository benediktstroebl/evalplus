
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
    count = 0

    if len(arr) <= 1:
        return count

    arr_val_map = {}

    for val in arr:
        if val in arr_val_map.keys():
            arr_val_map[val] += 1
        else:
            arr_val_map[val] = 1

    count = len(arr)

    for val in arr_val_map:
        if abs(arr_val_map[val] - len(arr) / 2) < count:
            count = abs(arr_val_map[val] - len(arr) / 2)

    return count
