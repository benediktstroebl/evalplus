```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2 - 1] + lst[n//2]) / 2
    else:
        return lst[n//2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4, 5]) == 5.0
assert median([5, 4, 3, 2, 1]) == 2.0
```