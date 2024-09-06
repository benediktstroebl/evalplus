```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test
def testMedian(testCase):
    testList = [1, 2, 4, 5]  # Even list
    assert median(testList) == 2.0  # Test even of even list
    testList = [3, 1, 2, 4, 5]  # Odd list
    assert median(testList) == 5.0  # Test of odd list

testMedian([])  # Test empty list
assert median([]), "Returned value is not empty"
```