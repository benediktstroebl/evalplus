```python
def median(l: list):
    """Return median of elements in the list l.
    return (sorted(l))[len(l) // 2] if len(l) % 2 == 0 else (l[len(l) // 2] + l[len(l) // 2 + 1]) / 2.0
   
   
```
def test_median():
    """Function to test the median function."""
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([9, 2, 1]) == 2.0
    assert median([10, 20, 40, 30]) == 20.0

test_median()