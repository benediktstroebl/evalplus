
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
    sorted_arr = sorted(arr)

    index_of_pivot = len(sorted_arr) // 2
    pivot = sorted_arr[index_of_pivot]

    if is_palindrome(sorted_arr):
        return 0

    return get_min_changes(sorted_arr, pivot)

