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
    # Calculate the list of changes required to make the array palindromic
    changes = []
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            changes.append(1)
        else:
            changes.append(0)
    # Return the minimum number of changes
    return min(changes)