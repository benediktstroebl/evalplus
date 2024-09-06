Here's the code:

```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not parse_error(x)]

seen = set()
uniq = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
assert uniq == [0, 2, 3, 5, 9, 123]
assert len(uniq) == 7  # Check length of unique list
```

This code defines a function called `unique` which takes a list as an argument and returns a new list containing only the unique elements from the original list. The function uses a set to keep track of the unique elements seen so far. The set is converted into a list to be able to access its elements by index. The function then iterates through the list and adds elements to the set if they are not in the set and are not `parse_error` calls.

The test cases ensure that the function is working correctly by passing the test lists and asserting that the resulting unique list has the expected elements.