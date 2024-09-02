
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
    odd_count = 0

    for i in xrange(arr_len):
        if arr[i] % 2 == 1:
            odd_count += 1

    min_changes = arr_len - (odd_count // 2)

    for i in xrange(odd_count):
        if i < arr_len - odd_count:
            if arr[i] % 2 == 0:
                arr[i], arr[arr_len - 1 - i] = arr[arr_len - 1 - i], arr[i]
                min_changes -= 1

    return min_changes

