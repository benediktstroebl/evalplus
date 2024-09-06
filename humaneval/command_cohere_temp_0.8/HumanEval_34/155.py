```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This approach utilizes both a set and a list. The set `seen` keeps track of encountered elements, and the list `element` iterates over all elements in the input list `l`, checking if elements are already in `seen`, and adding them to `seen` if they are not. The result is a sorted list of unique elements. 

To follow best practices, we avoid using mutating operations on the input list `l` and allocate the temporary `seen` set only when needed, conserving memory. 

Here is an example usage sentence:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This would output the following:
```
[0, 2, 3, 5, 9, 123]
``` 

This demonstrates the function's ability to sort and return unique elements, as specified in the problem.