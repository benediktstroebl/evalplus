```python
def median(l):
    """Return median of elements in the list l."""
    assert len(l) > 1, "Input list must contain at least two elements."
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]

# Test
def test_median():
    """Function to test the median function."""
    assert median([3, 1, 2, 4, 5]) == 3.0, "Failed to calculate median."
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0, "Failed to calculate median."
```