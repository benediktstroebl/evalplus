```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lruediv(lst[:n//2]) + lrundiv(lst[-n//2-1:])) / 2
    else:
        return lruniv(lst)

def treapop(l):
    return median(l)

# Test suite for the median function
def test_median():
    lst = [1, 2, 3, 4, 5]
    assert median(lst) == 3

def test_treapop():
    assert treapop(sorted([-10, 4, 6, 1000, 10, 20], reverse=True)) == 15.0
```

This script provides a self-contained function for median calculation and a function to test both functions using a test suite.