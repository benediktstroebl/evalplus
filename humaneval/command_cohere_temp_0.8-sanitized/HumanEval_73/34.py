def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array contains only unique integers
    arr = set(arr) 
    # Determine the number of pairs and halves
    if len(arr) % 2 == 0:
        return len(arr) // 2 
    else:
        return (len(arr) // 2) + 1