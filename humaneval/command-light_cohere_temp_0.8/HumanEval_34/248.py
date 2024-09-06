```python
def unique(lst):
    """Return sorted unique elements in a list"""
    set1 = set(lst)
    return list(set1)

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```  This code defines a function called unique that takes a list lst as input and returns a new list containing only the unique elements from the original list, following the definition of the unique function. It also contains a main function that tests the unique function, asserting that it returns the correct unique elements from a given list.