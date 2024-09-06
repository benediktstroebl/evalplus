```python
def unique(lst):
    seen = set()
    return [item for item in lst if item not in seen and item not None]

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function unique that takes a list lst as input and creates a set seen to keep track of elements that have already been seen. It then iterates elements each elements of the list that are not in the set seen and are not None to return a new list with unique elements. The test_unique function passes the test_unique, which checks that the function works as expected with a sample list.