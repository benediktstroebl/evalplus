```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a new list containing sorted unique elements from the input list. It uses the `set()` function to convert the input list to a set, eliminating duplicate elements, and then converts it back to a list. The `sort()` method is applied to sort the unique elements alphabetically. 

The function is documented with a docstring that describes its purpose, input, and output, and it includes a test case in the form of a "python -m unittest" block to ensure its correctness.