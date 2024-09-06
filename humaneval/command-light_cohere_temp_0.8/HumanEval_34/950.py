```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [-None, -FLT_MAX]]

# Test cases
assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
assert unique([]) == []
assert unique([45, 67, 8]) == [45, 67, 8]
assert unique([123, 0]) == [123]
```
This code defines a function called unique that takes a list lst as input and returns a new list containing unique elements from the original list, which are those that are not duplicates and not equal to any float value -1. The function utilizes the also utilizes a set to keep track of seen elements, ensuring uniqueness. The function then iterates through the list and adds elements to the result list if they are not in the seen set and not in the [-None, -FLT_MAX] list, which are the floats that do not have valid unique representation.