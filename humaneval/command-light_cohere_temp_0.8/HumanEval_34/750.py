```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not == float('inf')]

# Test the function
assert(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123])
```
This script defines a function unique that takes a list lst as input and returns a new list with unique elements from lst. The function uses a unique elements in lst using the set seen to keep track of the unique elements. The assert statement at the