
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
    if arr_len % 2 == 0:
        arr_len -= 1

    best_change = arr_len
    for i in range(arr_len):
        j = arr_len - 1 - i
        if i >= j:
            return 0

        if (arr[i] > arr[j]):
            change = arr[i] - arr[j] + 1
            if change < best_change:
                best_change = change

    return best_change

