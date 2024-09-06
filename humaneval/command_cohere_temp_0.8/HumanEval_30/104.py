```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers in that list. The function achieves this using a list comprehension, filtering out elements based on the condition `x > 0`.