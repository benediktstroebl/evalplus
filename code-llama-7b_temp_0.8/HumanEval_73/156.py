
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
    len_arr = len(arr)
    if len_arr == 0:
        return 0

    if len_arr == 1:
        return 0
    if len_arr == 2:
        if arr[0] == arr[1]:
            return 0
        return 1

    if len_arr % 2 == 1:
        return 1 + smallest_change(arr[1:])

    #  even size array
    smaller_count = 0
    for i in range(0, len_arr - 1):
        if arr[i] != arr[len_arr - 1 - i]:
            smaller_count += 1
    return smaller_count + smallest_change(arr[1:])
