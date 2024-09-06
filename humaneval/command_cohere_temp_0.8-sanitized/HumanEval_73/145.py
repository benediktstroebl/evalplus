def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        integer : Minimum number of changes required to make the array palindromic. 
    """
    # Ensure the array contains only unique integers
    arr = set(arr) 
    # Determine minimum changes required
    changes = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            # If the array isn't symmetric, increment count
            if arr[i] != arr[j]: 
                changes += 1
    return changes