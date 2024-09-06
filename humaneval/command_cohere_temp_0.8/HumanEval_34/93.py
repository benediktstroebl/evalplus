```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function called `unique` that takes a list `l` as an argument. It employs the `set()` function to remove duplicate entries from the input list and then uses the `sort()` function to organize the unique elements in ascending order. The function ultimately returns the sorted array of unique elements. 

The docstring at the start of the script provides a brief description of the function's purpose.

This solution is both efficient and well-documented, ensuring that it adequately addresses the problem statement and adheres to PEP 8, Python's coding standards. 

This approach allows you to efficiently and effectively sort and filter a list, ensuring uniqueness in the process with the added support of documentation for reference.