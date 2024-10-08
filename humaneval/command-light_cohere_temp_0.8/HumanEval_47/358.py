```python
def median(lst):
    """Return the median of list lst.
    return float((lst[(len(lst) + 1) // 2] + lst[len(lst) - 1]) / 2)

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4, 5]) == 4.0
assert median([]) == 0.0
assert median([10, 20, 30, 40]) == 20.0
```