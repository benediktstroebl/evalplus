```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called unique which takes one argument, l, which is a list. This function sorts the elements of l, removes any duplicates, and then returns the unique, sorted elements. 

The "Set" function creates a set of the list elements, which removes duplicates by design, and the resulting set of elements is then converted back into a list through list conversion. Subsequently, the 'sort' function sorts the list in ascending order. 

This effectively solves the problem of uniquely sorting a list of elements. Let's verify this with tests:
```python
def test_unique():
    # Test list with duplicates
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    
    # Test list with no duplicates
    assert unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test list with a single element
    assert unique([6]) == [6]
    
    # Test empty list
    assert unique([]) == []
```

Each test case represents a specific scenario that the unique function needs to handle, by checking if the return value is equal to the expected output.  This complete set of tests verifies the function unique and its different scenarios ensuring its correctness and providing confidence in its ability to handle various inputs.  The function unique is now confidently poised to solve the problem of removing duplicates and sorting a list of elements in a unique way.