```markdown
### Unique Elements in a List

This Python script defines a function `unique` that takes a list as input and returns a sorted list with unique elements.

```python
def unique(l: list):
    """
    Return sorted unique elements in a list

    Args:
    l (list): The input list

    Returns:
    list: A sorted list with unique elements

    Examples:
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Convert the list to a set to remove duplicates
    # Then convert it back to a list and sort it
    return sorted(list(set(l)))

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script uses the built-in `set` data structure in Python to remove duplicates and the `sorted` function to sort the resulting list in ascending order.

Alternatively, you can use a set comprehension to achieve the same result in a more concise way:

```python
def unique(l: list):
    """Return sorted unique elements in a list"""
    return sorted({i for i in l})

# Example usage
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

Both versions of the script will produce the same output: `[0, 2, 3, 5, 9, 123]`.