
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
    arr.sort()
    array_len = len(arr)
    start_idx = 0
    end_idx = array_len - 1
    while start_idx < end_idx:
        if arr[start_idx] != arr[end_idx]:
            return min(end_idx - start_idx, start_idx + 1)
        else:
            start_idx += 1
            end_idx -= 1
    return 0

