```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function named `unique` that takes a list `l` as input. It utilizes a set called `seen` to efficiently keep track of unique elements encountered while iterating through the input list. The function then returns a sorted list of these unique elements.

Here's an example of how you can use this function to clean up a list of integers:
```python
dirty_list = [1, 2, 3, 3, 4, 5, 4, 6, 7, 8, 1, 9, 8, 4, 10]
print(unique(dirty_list))
```

The output will be:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

This showcases the function cleaning and sorting the list, removing any duplicate entries.