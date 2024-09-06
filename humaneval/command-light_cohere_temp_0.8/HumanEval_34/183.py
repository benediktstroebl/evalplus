```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not in [0]]

# Tests
def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

test_unique()
```
This script defines a function `unique` that takes a list `lst` as input and returns a new list containing the unique elements from the original list. The function uses a unique() function, which is a built-in Python function that returns unique elements from a list, and it uses a set data structure to keep track of the elements that have been seen before. 
The test_unique function contains the test case for the `unique` function with a sample list.