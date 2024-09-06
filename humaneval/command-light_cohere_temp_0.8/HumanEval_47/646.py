```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) < 1:
        raise ValueError("Input list is empty.")
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test function
def testMedian(testList):
    assert median(testList) == (testList[-1] + testList[0]) / 2
```