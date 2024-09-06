```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[(n // 2) - 1]

# Test case
def test():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

test()
```