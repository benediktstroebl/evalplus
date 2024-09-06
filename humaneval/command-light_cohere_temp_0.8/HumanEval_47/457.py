```python
def median(lst):
    """Return the median value of a list l."""
    return median_impl(lst)[0]

def median_impl(lst):
    """Return the median value of a list l.
    return the median of the list if len(lst) < 3, return lst
    """
    n = len(lst)
    if n < 3:
        return lst
    m = lst[n//2] + lst[(n//2)-1]
    return median(m)

# Test cases
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```
This code defines a function median that calculates the median value of a list. The function median_impl is a helper function that recursively computes the median of a list. The main function median_impl handles the cases of an empty list or a list of length less than 3, returning the original list.  The test_median function tests the correctness of the median function.