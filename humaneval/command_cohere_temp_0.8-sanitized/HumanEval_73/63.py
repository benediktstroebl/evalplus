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
    
    # Initialize the change count to the array length
    changes = len(arr)
    
    # Loop through the array and reduce changes count if a duplicate element is found
    for num in arr:
        if num == arr.count(num):
            changes = changes - 1
    
    return changes