```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not float('inf')]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function `unique` that takes a list as input and returns a new list containing only the unique elements from the input list. The `seen` set is used to keep track of the elements we have encountered so far, and the function iterates through the input list using a generator expression to ensure all elements are processed. The test function `test_unique` verifies that the `unique` function correctly filters out duplicates.