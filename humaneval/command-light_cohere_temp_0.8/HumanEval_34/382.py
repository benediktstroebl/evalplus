```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return list(set(lst))

def test_unique():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
```
This code defines a function called unique, which takes a list as input and returns a new list containing only the unique elements from the original list. It also has a a test function test_unique() to ensure that the unique function works correctly on a sample input. 

This test passes the a list of numbers to the unique function and checks if the returned list contains all the expected unique elements.