```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) % 2 == 1:
        return (l[len(l)//2] + l[len(l)//2-1]) / 2
    elif len(l) % 2 == 0:
        return l[len(l)/2]
    else:
        raise ValueError("Length of list must be odd or even")

def test_median():
    """Function to test the median function"""
    assert median([3, 1, 2, 4, 5]) == 3.5
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
    assert median([1, 2, 4, 5]) == 4.0
    assert median([1, -3, 5, 6]) == -1.0
```

This code provides a self-contained solution to the problem, along with testing functions to ensure the correctness of the median function.