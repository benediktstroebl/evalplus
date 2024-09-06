```python
def median(l: list):
    """Return median of elements in the list l.
    assert(is_sorted(l)), 'The list is not sorted'
    assert len(l) > 1, 'The list must contain at least two elements'
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Tests if the function
# correctly calculates median
def test_median():
    """Test the median function."""
    l = [-10, 4, 6, 1000, 10, 20]
    assert median(l) == 15.0, "The median is incorrect"
```