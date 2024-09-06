```python
def median(lst):
    """Return median of elements in the list lst."""
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    if len(lst) % 2 == 0:
        return (lst[len(lst)//2 - 1] + lst[len(lst)//2]) / 2
    else:
        return lst[len(lst)//2]

#Test suite for median function
def testMedian():
    try:
    # Test list with positive and negative numbers, empty list, and complex numbers
    lst = [3, 1, 2, 4, 5, -10, 4, 6, 1000, 10, 20, (3+4i)]
    assert median(lst) == 15.0
    except:
        raise AssertionError("Returned value is not the expected median.")

# Test suite for basic cases
testMedian()()
```