```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
The code defines a function `unique` that takes a list `lst` as input and returns a new list containing only the unique elements from the original list. This is unique elements is achieved using a set to keep track of elements that have been encountered before. The function iterates through each item in the input list and adds it to the set if it is not in the set and is not `None`. 

The function then returns a new list containing only the elements that are not in the set and not `None`.