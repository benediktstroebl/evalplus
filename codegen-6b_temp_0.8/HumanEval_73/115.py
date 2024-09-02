
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
    N = len(arr)
    # Repeat the array twice and check for palindromicity
    if N % 2 == 0:
        # Odd length, just double the input + check for palindromicity
        limit = 2 * N
    else:
        # Even length, double the input + use half the array
        limit = (2 * N) + 1
    for i in range(limit):
        arr_copy = arr[:]
        arr_copy[i // 2] = (arr_copy[i // 2] + 1) % 10
        if arr_copy == arr_copy[::-1]:
            return i

    return -1

