```python
def median(lst):
    """Return the median of elements in list lst."""
    try:
        m = len(lst) // 2 + 1
        if len(lst) % 2 == 0:
            return (lst[m - 1] + lst[m]) / 2
        else:
            return lst[m]
    except IndexError:
        return "Index out of range"

# Test suite
def testMedian():
    assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Another test with an empty list
testMedian()
```