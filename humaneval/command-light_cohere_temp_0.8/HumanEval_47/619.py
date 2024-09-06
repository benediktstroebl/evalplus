```python
def median(l):
    """Return median of elements in the list l."""
    return float('median'([x for x in l if type(x) == int]))
# tests
def testMedian(func):
    list1 = [1, 2, 4, 5]
    list2 = [-10, 4, 6, 1000, 10, 20]
    assert func(list1) == 3.0 and func(list2) == 15.0, True
```