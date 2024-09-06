```python
def median(l):
    """Return median of elements in the list l."""
    if len(l) % 2 == 1:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[len(l) // 2]

# Test
def testMedian(testList):
    assert median(testList) == (testList[-1] + testList[0]) / 2

# Test with even length list
testMedian([-10, 4, 6, 1000, 10, 20])

# Test with single element list
testMedian([1000])
```