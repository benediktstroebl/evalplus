
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
    if len(arr) == 1:
        return 0

    if len(arr) == 2:
        return abs(arr[0] - arr[1])

    palindromic_arr = get_palindromic_arr(arr)
    # Change the minimum element to make the array palindromic
    if len(palindromic_arr) == 1:
        return abs(arr[0] - arr[1])
    elif len(palindromic_arr) == 2:
        return min(abs(arr[0] - arr[1]), abs(arr[0] - arr[1]))
    else:
        return min(abs(arr[0] - arr[1]), abs(arr[0] - arr[1]), abs(arr[0] - palindromic_arr[1]))

