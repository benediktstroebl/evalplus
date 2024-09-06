```python
def median(lst):
    """Return median of elements in the list lst."""
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2 - 1)::2][0] + lst[(n//2)][0]) / 2
    else:
        return lst[n//2][0]

# Test suite for median function
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 4, 3, 2, 5]) == 4.0
    assert median([10, 20, 30, 10, 40]) == 15.0
    assert median([1, 2, 3, 4, 5]) != median([3, 1, 2, 4, 5])
```