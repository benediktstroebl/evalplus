```markdown
### below_threshold Function
#### Returns True if all numbers in the list are below the threshold
```python
def below_threshold(l: list, t: int):
    """
    Return True if all numbers in the list l are below threshold t.

    Args:
    l (list): A list of numbers to check.
    t (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.

    Example:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # Use the built-in all() function and a generator expression to check if all numbers in the list are below the threshold
    return all(i < t for i in l)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```
In this script, the `below_threshold` function uses the `all()` function and a generator expression to check if all numbers in the list are below the threshold. The `all()` function returns `True` if all elements of the iterable are true. If at least one element is false, `all()` returns `False`.