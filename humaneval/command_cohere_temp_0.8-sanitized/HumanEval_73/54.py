def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes required to make the array palindromic
    """
    # Ensure the array contains only unique elements
    arr = list(set(arr))
    # Calculate reverse of array
    rev_arr = sorted(arr)[::-1]
    return sum((x != y for x, y in zip(arr, rev_arr)))