```python
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
```

The function operates by initializing the variable `smallest_change` to a large value, `float('inf')`, to handle cases where the minimum number of changes might approach infinity. It first checks if the length of the array is odd, which is not palindromic, and returns half the length if it's odd. The function then loops through the array, checking if elements are already in the correct mirror position, and calculates the number of changes needed for each element that isn't. It updates the `smallest_change` with the minimum value encountered. Finally, the function returns the `smallest_change`. 

The function elegantly avoids explicit looping through the mirror positions of the array by utilizing the `len(arr) - 1 - i` calculation for the mirror position. 

This solution avoids the use of nested loops, making the code more efficient and easier to read. It also doesn't require any extra space beyond what's needed to return the result.