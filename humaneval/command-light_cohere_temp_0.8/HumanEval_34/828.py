```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == 0]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert not unique([0])
assert not unique([5, 3, 'x', 5])
``` 
This code defines a unique function that takes a list as an argument and returns a list of unique elements from that list, excluding 0. The function utilizes a set to keep track of seen elements and then iterates over the input list, adding elements that are not in the set and not equal to 0.