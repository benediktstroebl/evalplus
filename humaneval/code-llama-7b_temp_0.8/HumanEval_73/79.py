
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
    # palindrome can be defined by two properties:
    # (1) number of distinct numbers is odd
    # (2) at the middle, the first and last number are the same

    distinct_numbers = set(arr)
    distinct_numbers_count = len(distinct_numbers)

    if distinct_numbers_count % 2 == 0:
        return 0

    # check if the middle element is the same as first and last
    middle_idx = len(arr) // 2

    if arr[middle_idx] != arr[0] or arr[middle_idx] != arr[len(arr) - 1]:
        return 1

    return 2
