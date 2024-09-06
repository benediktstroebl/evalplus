
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

    # step 1 - check for edge cases
    if len(arr) == 1 or arr == arr[::-1]:
        return 0
    # step 2 - get the array reversed, for the palindrome
    arr_reverse = arr[::-1]
    # step 3 - check if the array is palindrome
    for i, j in zip(arr, arr_reverse):
        if i != j:
            return len(arr_reverse)

