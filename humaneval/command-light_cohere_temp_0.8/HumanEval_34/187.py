```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This script defines a function unique that takes a list as input and returns a new list with unique elements from the original list. The function uses a set to keep track of seen elements, then iterates over the original list and adds elements to the list if they are not in the set and are not None.

The test_unique function tests the function by passing a known list of values and asserts that the returned list contains the expected elements.