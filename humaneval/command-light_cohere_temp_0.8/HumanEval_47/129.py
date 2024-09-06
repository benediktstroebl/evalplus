```python
def median(lst):
    """Return the median of list lst."""
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]

# Test the function with a sample list
test_median = lambda: median([-10, 4, 6, 1000, 10, 20]) == 15.0
test_median()
```

This script defines a function median that computes the median of a list. The function handles both cases: cases where the length of the list is even and the odd case. The median is calculated as the average of the two middle numbers or taking the middle number. The test function is used to verify that the median function returns the correct result for a given list.