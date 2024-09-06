def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required
    """
    # Ensure the array contains only unique integers
    arr = list(set(arr))
    # Create a reversed copy of the array
    rev = arr[::-1]
    # Count number of changes required
    change = 0
    for a, b in zip(arr, rev):
        # If the two elements are not equal, increment the change count
        if a != b:
            change += 1
    return change