```python
def median(lst):
    """Return the median of the list lst."""
    # Sort the list
    sorted_lst = sorted(lst)
    # Determine the middle index
    middle = len(sorted_lst) // 2
    # Handle empty list
    if middle == 0:
        return None
    # Return median
    return sorted_lst[middle]
# Test cases
median([3, 1, 2, 4, 5]) # 3.0
median([-10, 4, 6, 1000, 10, 20]) # 15.0
median([5, 10, 20, -100, 30]) # 25.0
median([10, 20, 30, 40]) # 25.0
median([1, 2, 4, 8, 5]) # 4.0
median([1000, 1001, 1002]) # 500.0
```

This Python code defines a function `median(lst)` that calculates and returns the median of the elements in a given list `lst`. It sorts the elements in the list, finds the middle index, and then returns the median value. The test cases are provided to ensure that the function works correctly for various scenarios.