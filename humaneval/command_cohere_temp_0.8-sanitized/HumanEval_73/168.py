def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        Minimum number of changes
    """
    # Ensure the array has even length
    if len(arr) % 2 == 1:
        return len(arr) - 1
    
    # Initialize the two resulting arrays: current and reverse
    curr = arr.copy()
    rev = arr[::-1]
    
    # Initialize the result to the maximum possible value
    result = len(arr) - 1
    
    # Loop through the elements in the array
    for i in range(len(arr)):
        # Calculate the number of changes needed to make the current element the same as its counterpart in the reverse array
        change = abs(curr[i] - rev[i])
        
        # Update the result if the current change is less than the current result
        result = min(result, change)
        
        # Update the current array to remove the current element and add the reverse element
        curr = arr[:i] + arr[i+1:i] + [rev[i]] + arr[i+1:]
    
    return result