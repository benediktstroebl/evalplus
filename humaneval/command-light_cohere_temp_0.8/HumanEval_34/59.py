```python
def unique(lst):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

#Test case 1
def test1():
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

#Test case 2
def test2():
    assert unique([]) == []
```
The code defines a function unique that takes a list as input and returns a new list with unique elements from the original. This function uses the simple set() to remove duplicates and then returns the sorted list of unique elements. The test cases demonstrate the case 1 and 2 correctly pass the assertions.