```python
def median(l):
    """Return median of elements in the list l."""
    from statistics import median
    return median(sorted(l))

# Testing the function
def testMedian(testList):
    """Test function to test the median function."""
    assert median(testList) == 6.0, "Wrong median value!"

# Example usage
testList = [
     [-10, 4, 6, 1000, 10, 20],
    [20, 18, 16, 14, 12, 10],
    [0, 0, 0]
]
testMedian(median)
```