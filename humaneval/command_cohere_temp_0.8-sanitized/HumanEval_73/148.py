def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Sort the array
    sorted_arr = sorted(arr)
    # Get the number of elements at the start and end of the array
    left, right = sorted_arr[:1], sorted_arr[-1:]
    # Calculate the minimum number of changes
    change_count = abs(len(left) - len(right))
    return change_count