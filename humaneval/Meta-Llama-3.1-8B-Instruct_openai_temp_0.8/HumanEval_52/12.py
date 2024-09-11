```markdown
### below_threshold function
#### Return True if all numbers in the list l are below threshold t.

```python
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
        l (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers in the list l are below threshold t, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < t for num in l)
```

### Explanation

This function uses Python's built-in `all()` function to check if all numbers in the list `l` are below the threshold `t`. The `all()` function returns `True` if all elements in the iterable (in this case, the generator expression) are true.

The generator expression `(num < t for num in l)` generates a sequence of boolean values indicating whether each number in the list is below the threshold.

### Example Use Cases

```python
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```