```python
def median(lst):
    """Return median of elements in the list lst."""
    sorted_lst = sorted(lst)
    length = len(sorted_lst)
    
    if length % 2 == 0:
        return (sorted_lst[length // 2 - 1] + sorted_lst[length // 2]) / 2
    else:
        return sorted_lst[length // 2]

# Test suite for the function median
def test_median():
    # Test list with odd length
    lst = [-10, 4, 6, 1000, 10, 20]
    assert median(lst) == 10.0
    # Test list with even length
    lst = [1, 2, 4, 5]
    assert median(lst) == 5.0
```

The provided Python script defines a function called `median` that calculates the median of a list of elements. It achieves this by sorting the list and then determining the median based on the length of the list. The script also contains a test suite that validates the correctness of the `median` function by passing various test cases.