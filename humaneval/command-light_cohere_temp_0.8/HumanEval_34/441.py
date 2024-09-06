```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list lst as input and returns a new list containing only the unique elements from the original list. It uses a str. set of set to keep unique elements in the list and returns a new list with the unique elements. The test_unique function passes the result of calling the unique function with the test list and verifies that it returns the expected output.