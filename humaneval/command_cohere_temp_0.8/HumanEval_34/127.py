```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    seen = set()
    result = [x for x in l if not (x in seen or seen.add(x))]
    return sorted(result)
```

This Python script defines a function named `unique` that takes a list `l` as input. It utilizes a set called `seen` to efficiently keep track of unique elements encountered while iterating through the input list. The function employs a list comprehension to filter elements that have not already been seen or added to the `seen` set, thereby ensuring only unique elements are included in the `result` list. Lastly, the function sorts the `result` list before returning the sorted unique elements.

Here's an example of how you can use the unique function to clean a list of duplicates:
```python
dirty_list = [7, 2, 3, 4, 7, 5, 6, 2, 8, 7, 9, 3, 10]
clean_list = unique(dirty_list)
print(clean_list)
```

Output:
```bash
[2, 3, 4, 5, 6, 7, 8, 9, 10]
```

This showcases the function's ability to remove duplicates, sorting the unique elements in the process.