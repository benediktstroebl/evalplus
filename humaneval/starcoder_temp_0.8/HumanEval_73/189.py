
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
    # Go through array and count number of odds
    odd_count = 0
    for num in arr:
        if num % 2!= 0:
            odd_count += 1

    # Return number of odds if odd_count is odd, otherwise return 0
    return odd_count if odd_count % 2!= 0 else 0
