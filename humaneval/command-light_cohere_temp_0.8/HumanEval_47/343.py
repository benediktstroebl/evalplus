```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (lst[n // 2] + lst[n // 2 - 1]) / 2
    else:
        return lst[(n // 2) - 1]

# Test cases
tests = [median([3, 1, 2, 4, 5]), median([-10, 4, 6, 1000, 10, 20])]

print(tests)
```