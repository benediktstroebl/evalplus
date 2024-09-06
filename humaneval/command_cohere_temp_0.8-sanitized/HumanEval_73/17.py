def smallest_change(arr):
    # Sort the input array
    arr.sort()
    
    # Initialize a counter for changes
    count = 0
    
    # Iterate through the array after sorting
    for i in range(1, len(arr)):
        # Check if the current element is different from the previous one
        if arr[i] != arr[i-1]:
            # If different, increment the change counter
            count += 1
    
    # Return the final count of changes required
    return count