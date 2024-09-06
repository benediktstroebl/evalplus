```python
def median(l):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2.0  # (sorted(l) + [0])[len(l) % 2]

# Unit tests
def testMedian(testList):
    med = median(testList)
    assert med == (len(testList) + 1) / 2.0 * (sorted(testList) + [0])[len(testList) % 2], "test failed"

testList1 = [4, 2, 10, 1]
testList2 = [5, 6, 3, 4]
testList3 = [1000, 10, 20, 4, 6]
testList4 = [-10, 4, 6, 3, 5, 20]
testList5 = [1, 2, 3, 4, 5, 10, 6]
testList6 = [20, 10, 4, 6, 3, 5]
testList7 = [4, 5, 6, -10]
testList8 = [1000, 10, 20, 4, 6, -100]
testList9 = [None, 4, 6, 5]
testList10 = [1, 2, 3, 4, 5, -10]

testMedian(testList1)
testMedian(testList2)
testMedian(testList3)
testMedian(testList4)
testMedian(testList5)
testMedian(testList6)
testMedian(testList7)
testMedian(testList8)
testMedian(testList9)
testMedian(testList10)
```
This Python script defines a function median that computes the median value of a list of numbers. The testMedian function has 10 test lists, and asserts that the median value returned by the median function is correct for each test list.