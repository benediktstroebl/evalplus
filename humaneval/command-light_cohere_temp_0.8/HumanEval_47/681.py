```python
def median(lst):
    """Return median of elements in the list lst."""
    return (len(lst) + 1) * (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

# Test case 1
if median([3, 1, 2, 4, 5]) != 3:
    raise ValueError("Error: Median is not calculated correctly.")

# Test case 2
if median([-10, 4, 6, 1000, 10, 20]) != 15.0:
    raise ValueError("Error: Median is not calculated correctly.")

# Test case 3
if median([1, 2, 4, 5, 6]) != 5:
    raise ValueError("Error: Median is not calculated correctly.")
```