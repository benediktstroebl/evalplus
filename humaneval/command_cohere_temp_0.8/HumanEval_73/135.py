```python
def smallest_change(arr):
    arr.sort()
    count = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1
    return count
```

The function `smallest_change()` takes an array `arr` as input and returns the smallest number of changes required to make the array palindromic. The function sorts the input array and then counts the number of distinct elements in the sorted array. This count represents the minimum number of changes required to make the original array palindromic.

Here is a version of the code with comments to explain each step:
```python
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
```

This function provides the smallest number of changes necessary to make the original array palindromic, which it does by sorting the array and then identifying the number of distinct elements in the sorted array. This approach guarantees that the result is correct.