```markdown
### below_threshold Function
#### Returns True if all numbers in the list are below threshold.

```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        numbers (list): A list of integers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.

    Examples:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in numbers)
```

### Example Usage
```python
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

### Explanation
The `below_threshold` function uses the built-in `all()` function in combination with a generator expression to check if all numbers in the list are below the specified threshold. The `all()` function returns `True` if all elements in the iterable are true, and `False` otherwise.