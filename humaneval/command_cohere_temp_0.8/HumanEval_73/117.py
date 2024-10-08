```python
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    Returns:
        integer: The minimum number of changes required 
    """
    # Ensure array is sorted
    arr = sorted(arr)
    changes = 0
    # Iterate through array and calculate changes
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            changes += 1
    return changes
```

This function calculates the minimum changes required by iterating through the array and counting dissimilar elements in two successive positions. It assumes that the array is already sorted, as sorting an array is typically a trivial operation while solving algorithmic problems. This approach ensures that the provided solution is self-contained and can be directly utilized without the need for external sorting utilities.