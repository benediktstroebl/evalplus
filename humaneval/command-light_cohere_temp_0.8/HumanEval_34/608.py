```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code provides a function unique that takes a list lst as input and returns a new list with unique elements from the original list. This is unique elements is not present in the original list and is not None. The function utilizes the certain test data structure seen to keep track of elements that have been encountered. It then loops over the done list, and adds each element to the seen set. This ensures that all previously encountered elements are not added again, effectively picking out the list's unique elements. The test_unique function then verifies that the output of unique is indeed the expected unique elements from the original list.