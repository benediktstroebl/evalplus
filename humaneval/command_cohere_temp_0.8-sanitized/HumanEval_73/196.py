def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Initialize the result to the length of the array
    result = len(arr)
    # Iterate over the array from the first to the last element
    for i in range(len(arr)):
        # Iterate over the array from the last to the first element
        for j in range(len(arr)-1, -1, -1):
            # If the current elements are not equal, count it as a change
            if arr[i] != arr[j]:
                result = min(result, 2)
                if result == 0:  # If the result is zero, break the internal loop
                    break
    return result