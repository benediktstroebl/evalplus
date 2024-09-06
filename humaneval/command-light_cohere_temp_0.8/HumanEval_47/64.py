```python
def median(l):
    """Return median of elements in the list l."""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test suite for median function
def testMedian():
    """Function test for median."""
    testList = [
        -10, 4, 6, 1000, 10, 20, 2, 1, \
        30, 33, 22, 19, 21, 17
    ]

    assert median(testList) == 15.0, "The median is not 15.0"
    expected output.