```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test case 1
assert median([3, 1, 2, 4, 5]) == 3

# Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 3
assert median([2, 4, 6, 8, 10]) == 4

# Test case 4
try:
    assert median([10, 10, 10]) == 10
except AssertionError as e:
    print(f"Error: {e}" )
```