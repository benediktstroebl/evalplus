
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

    # base case
    if len(arr) < 2:
        return 0
    if len(arr) == 2:
        return 1 if arr[0] == arr[1] else 2

    # 2 or more elements
    min_count = len(arr)
    for i in range(0, len(arr)):
        # Find a palindrome in the subarray that contains the element at index i
        min_count = min(min_count, min_count_helper(arr, i))

    return min_count

