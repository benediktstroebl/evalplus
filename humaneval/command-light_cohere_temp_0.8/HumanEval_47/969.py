```python
def median(l: list):
    """Return median of elements in the list l.
    if len(l) % 2 == 1:
        return l[len(l)//2]
    else:
        return (l[len(l)//2-1] + l[len(l)//2]) / 2

def test_median():
    """Function to test the median function"""
    assert median([3, 1, 2, 4, 5]) == 3.0
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 3, 4, 5]) == 3.0
    assert median([10, 20, 30, 40]) == 20.0

test_median()
```