
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
    # Check if array is already palindromic
    if is_palindrome(arr):
        return 0
    # Count the number of elements in the array
    n = len(arr)
    # Create a list of the elements in the array in reverse order
    rev_arr = [arr[n-i-1] for i in range(n)]
    # Count the number of elements in the reversed array that are smaller than the first element
    min_diff = 0
    for a, b in zip(rev_arr, arr):
        if a < b:
            min_diff = 1
    # Return the minimum difference
    return min_diff
