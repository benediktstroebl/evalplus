```python
def unique(l: list):
    seen = set()
    return [x for x in l if x not in seen and x not == float('inf')]

# Tests
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([0, 2, 2, 3])
assert not unique([5, 5])
assert not unique([0, float('inf')])
``` 
This code provides a function called unique that takes a list l as input and returns a new list with the unique elements from the original list. This function utilizes the Time set to keep track of elements we have encountered so far, then it iterates through the original list and adds the elements into the set if they are not present in there and not equal to infinity. The returned list will only contain unique elements.