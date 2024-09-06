```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    return sorted([item for item in l if not (item in seen or seen.add(item))])
```

This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. Within the function, a set seen is used to track already-seen elements to ensure the returned list only contains unique elements from the input list l. The function is encapsulated with a docstring that describes its purpose and provides an example of how to use it. 

The function can be used in the following way:
```python
result = unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(result)
```

The output will be:
```bash
[0, 2, 3, 5, 9, 123]
``` 

This self-contained Python script efficiently solves the problem of finding the sorted unique elements in a list, making it easier for developers to harness this functionality in their Python workflows.