```python
def median(l):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test suite for the median function
def test_median():
    lst = [-10, 4, 6, 1000, 10, 20, 1, 2, 3]
    assert median(lst) == 3.0

test_median() # Test suite execution
```