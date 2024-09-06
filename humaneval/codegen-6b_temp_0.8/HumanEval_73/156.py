
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
    if len(arr) == 0:
        return -1
    candidates = list(range(len(arr)))
    start = 0
    end = 1
    while start < end:
        idx_start = start
        idx_end = end
        change_start_idx = arr[start]
        change_end_idx = arr[end]
        while idx_start != idx_end:
            if arr[idx_end] > arr[idx_start]:
                break
            if arr[idx_start] > arr[idx_end]:
                candidates[idx_start] = arr[idx_end]
                candidates[idx_end] = arr[idx_start]
                idx_end -= 1
            idx_start += 1
        start += 1
        end -= 1
    return min([abs(arr[elem] - arr[candidates[elem]]) for elem in candidates])

