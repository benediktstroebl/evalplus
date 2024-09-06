
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
    arr_sorted = sorted(arr)
    arr_sorted_set = list(set(arr_sorted))
    arr_sorted_set.reverse()
    if arr_sorted == arr_sorted_set:
        return 0
    else:
        size = len(arr)
        start_count = arr_sorted.count(arr[0])
        end_count = arr_sorted.count(arr[-1])
        if start_count < size:
            return size - start_count
        else:
            return size - end_count

