```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This code uses a set, `seen`, to keep track of unique elements, allowing it to efficiently filter out duplicates while maintaining order. The use of `element for element in l if ...` generates a list of unique elements, which is then sorted using the `sorted()` function. The docstring at the beginning of the code correctly describes the functionality of the `unique` function. 

To see this function in action, you can call it with the example list provided in the problem statement: 
```python
unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
```

This will output a sorted list of unique elements as expected:
```bash
[0, 2, 3, 5, 9, 123]
``` 

This approach efficiently solves the problem while maintaining the elegance and readability of Python.