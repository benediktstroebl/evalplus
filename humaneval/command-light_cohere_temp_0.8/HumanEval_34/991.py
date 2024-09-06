```python
def unique(l: list):
    return list(set(l))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list l and returns a new list with unique elements from l. The test_unique function passes the test_unique() evaluates to True, which demonstrates that the unique function successfully returns unique elements from the input list.