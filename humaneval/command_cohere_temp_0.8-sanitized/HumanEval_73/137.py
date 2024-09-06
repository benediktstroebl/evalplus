def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required 
    """
    # Ensure the array has duplicates
    arr = list(set(arr))
    
    # Ensure the array has an even length
    if len(arr) % 2 == 1:
        return len(arr) // 2 + 1
    
    # Calculate the midpoint
    mid = len(arr) // 2
    
    # If the start and end halves are the same, return 0
    if arr[:mid] == arr[mid:]:
        return 0
    
    # Count the number of common elements in the start and end halves
    crossover_count = len(arr) - len(list(set(arr[:mid] + arr[mid:])))
    
    return min(crossover_count, mid)