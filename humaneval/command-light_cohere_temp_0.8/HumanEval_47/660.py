```python
def median(lst):
    """Return the median of list l."""
    # Sort the list in ascending order
    lst.sort(lst)
    # Take the middle element (length of the sorted list is even)
    middle = len(lst) // 2
    if len(lst) % 2 == 0:
        return (lst[middle] + lst[middle - 1]) / 2
    else:
        return lst[middle]

# Unit tests
def testMedian():
    assert median([3, 1, 2, 4, 5]) == 3.0

# Test edge cases
assert median([]) == 0
assert median([10, 10, 10]) == 10
assert median([10, 20, 30]) == 15

# Test list of negative numbers
assert median([-10, 4, 6, 1000, 10, 20]) == -10

testMedian()
```