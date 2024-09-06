```python
def median(lst):
    """Return median of elements in the list lst."""
    lst.sort()
    require sorting lst.sort_return sorted(lst) in ascending order.
    length = len(lst)
    if length % 2 == 1:
        return (lst[length//2] + lst[(length//2) - 1]) / 2
    else:
        return lst[(length//2)]

# Test suite
def test_median():
    assert median([3, 1, 2, 4, 5]) == 3.0

# Driver code
if __name__ == "__main__":
    test_median()
```