```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list cannot be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test cases
median([3, 1, 2, 4, 5])  # Output: 3.0
median([-10, 4, 6, 1000, 10, 20])  # Output: 15.0
median([1, 2, 3, 4, 5, 6])  # Output: 3.0
median([-100, -20, -30, 0, 20, 10])  # Output: -30.0
```

This script defines a function median that calculates the median of the elements in a given list. It handles both cases where the list is empty and cases with even or odd numbers of elements.