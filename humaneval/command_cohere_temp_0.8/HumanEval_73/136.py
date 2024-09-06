```python
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
```

The algorithm for the problem uses two nested loops to compare each element in the array to its counterpart going in opposite directions. The result variable is initialized to the length of the array, and for each comparison that indicates a change (non-matching elements), the result is updated to the minimum value between the current result and 2, indicating the minimum number of changes required. The inner loop is terminated if the result reaches zero, indicating the palindromic symmetry is reached and no further changes are required.