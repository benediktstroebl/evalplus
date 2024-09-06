def smallest_change(arr):
    # Sort the input array
    arr.sort()
    
    # Initialize the count of changes
    count = 0
    
    # Loop through the sorted array
    for i in range(1, len(arr)):
        # Check if the current element is different from the previous one
        if arr[i] != arr[i-1]:
            # If different, increment the change count
            count += 1
    
    # Return the final count of changes
    return count