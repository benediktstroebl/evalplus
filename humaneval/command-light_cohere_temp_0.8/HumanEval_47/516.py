```python
def median(lst):
    """Return the median of list lst."""
    if len(lst) % 2 == 0:
        return (lst[(len(lst) / 2) - 1] + lst[len / 2]) / 2
    else:
        return lst[(len(lst) - 1) // 2]

# Test
def test_median():
    return median([-10, 4, 6, 1000, 10, 20]) == 15.0
```