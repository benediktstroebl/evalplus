
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
    arr_len = len(arr)
    start = 0
    end = arr_len - 1
    smallest_change_count = 999999

    while start < end:
        smallest_change_count = min(smallest_change_count,
                                    abs(arr[start] - arr[end]))

        if arr[start] > arr[end]:
            start += 1
        else:
            end -= 1

    return smallest_change_count


assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 1]) == 0
assert smallest_change([1, 2, 3, 4, 3, 2, 2]) == 4
assert smallest_change([1, 2, 3, 4, 3, 2, 5]) == 2
assert smallest_change([1, 2, 3, 2, 1, 2, 3, 2, 1, 2]) == 4
assert smallest_change([1, 2, 3, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2]) == 2
assert smallest_change([1, 2, 3, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2]) == 2
assert smallest_change([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2]) == 1
assert smallest_change([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2]) == 2
assert smallest_change([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2]) == 2
assert smallest_change([1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 2]) == 2
assert smallest_