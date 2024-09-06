
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

    if not arr:
        return 0

    arr_len = len(arr)
    if arr_len == 1:
        return 0

    start_idx = 0
    end_idx = arr_len - 1

    count = 0
    while start_idx < end_idx:
        if arr[start_idx] == arr[end_idx]:
            start_idx += 1
            end_idx -= 1
        else:
            start_idx += 1
            count += 1

    return count + (arr_len - 2 * start_idx)

