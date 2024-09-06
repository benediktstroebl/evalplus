def smallest_change(arr):
    # Initialize the smallest change to an arbitrary large value
    smallest_change = float('inf')

    # Check if the length of the array is odd, which is not palindromic
    if len(arr) % 2 != 0:
        return len(arr) // 2
    
    # Iterate through the array
    for i in range(len(arr)):
        # Check if the element is already in the mirror position
        if arr[i] == arr[len(arr) - 1 - i]:
            continue
        # Calculate the number of changes by subtracting 2 from the difference in positions
        change_needed = abs(i - (len(arr) - 1 - i)) + 1
        smallest_change = min(smallest_change, change_needed)
    
    return smallest_change