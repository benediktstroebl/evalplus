```python
def median(l):
    """Return median of elements in the list l."""
    return (getattr(sorted(l))[len(l)//2]) if len(l) % 2 == 1 else (get_median(sorted(l[:len(l)//2)) + sorted(l[-len(l)//2:])))

def get_median(l):
    """Return the median of a list using stable sort."""
    return (sorted(l), l)[len(l)//2]

def test_median():
    """A test function to check the correctness of median function."""
    assert median([1,2,3]) == 2
    assert median([3,1,4]) == 2
    assert median([-10, 4, 6, 1000, 10, 20]) == 15
    assert median([10, -10, 20, -20]) == 15
    assert median([3, 4, 5, 6]) == 5
    assert median([-1, 2, 3, 4]) == 2
```