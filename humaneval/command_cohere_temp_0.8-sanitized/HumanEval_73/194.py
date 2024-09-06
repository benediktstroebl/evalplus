def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        int: The minimum number of changes required.
    """
    # Ensure the array contains only unique integers.
    arr.sort()
    arr = list(set(arr))
    
    # Create a map of the index to the number of occurrences in the original array.
    occurances = {}
    for i, n in enumerate(arr):
        occurances[n] = occurances.get(n, 0) + 1
    
    # Create a list of indices to iterate through, considering only the last occurrence of each number.
    indices = [value for value, _ in occurances.items()]
    
    # Calculate the midpoint to reduce the number of iterations.
    mid = len(arr) // 2
    
    # Initialize the smallest change to infinity.
    smallest_change = float('inf')
    
    for start, n in enumerate(arr, 1):
        # Calculate the index of the last occurrence of n in arr.
        end = indices.index(n) + mid
        
        if start > end:
            continue
        
        # Calculate the smallest change involving element n.
        change = min(abs(start - end) - 1, smallest_change)
        
        # Update the smallest change if the change involving n is smaller.
        smallest_change = min(smallest_change, change)
    
    return smallest_change