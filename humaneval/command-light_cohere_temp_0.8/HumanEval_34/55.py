```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
The unique function takes a list as input and returns a new list containing only the unique elements from the input list. The function uses a input list and a set to keep track of seen elements. Then, it iterates over the unique elements and adds them to the output list if they are not in the set. Finally, the function returns the list.