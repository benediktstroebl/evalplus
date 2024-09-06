```python
def median(lst):
    """Return the median of elements in the list lst."""
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]
# Test the function
def test_median():
    list1 = [-10, 4, 6, 1000, 10, 20]
    assert median(list1) == 15.0
```