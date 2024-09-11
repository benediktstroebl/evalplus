```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.

    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` which takes a list of numbers and a threshold value. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The result is then returned as a boolean value. The function is documented with a docstring that includes a description, arguments, return value, and examples of usage.