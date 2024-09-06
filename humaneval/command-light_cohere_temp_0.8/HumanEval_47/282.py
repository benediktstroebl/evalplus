```python
def median(lst):
    """Return the median value of elements in list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[(n - 1) // 2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([-100, -200, -300]) == ( -200 + 100 ) / 2 
assert median([10, 20, 30]) == 15
assert median([]) == ""  # Empty list
```