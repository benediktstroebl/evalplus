```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2 - 1)] + lst[n//2]) / 2
    else:
        return lst[(n//2)]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([1, 2, 3, 4]) == 3
assert median([10, 20, 3, 2, 1]) == 3
assert median([]) == 0
assert median([10, 20, 10, 20]) == 10
```