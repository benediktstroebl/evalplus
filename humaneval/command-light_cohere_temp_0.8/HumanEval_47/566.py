```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[(n - 1) // 2]

# Test cases
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0

test_median()
```