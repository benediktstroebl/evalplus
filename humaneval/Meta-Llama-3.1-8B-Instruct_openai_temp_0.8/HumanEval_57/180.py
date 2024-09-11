```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
    lst (list): A list of numbers.

    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    increasing = decreasing = True
    
    for i in range(1, len(lst)):
        # Check if list is decreasing
        if lst[i] > lst[i - 1]:
            decreasing = False
        # Check if list is increasing
        if lst[i] < lst[i - 1]:
            increasing = False
            
    # Return True if list is either increasing or decreasing
    return increasing or decreasing

# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

In this script, we define a function `monotonic` that checks if a list is monotonically increasing or decreasing. We use two flags, `increasing` and `decreasing`, initialized to `True`, to track whether the list is increasing or decreasing. We then iterate over the list and check if each pair of adjacent elements satisfies the conditions for increasing or decreasing. If we find a pair that doesn't satisfy the conditions, we set the corresponding flag to `False`. Finally, we return `True` if either flag is still `True`, indicating that the list is either increasing or decreasing.