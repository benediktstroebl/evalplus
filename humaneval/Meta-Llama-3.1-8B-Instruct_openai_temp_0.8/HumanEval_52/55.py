```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.
    
    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)


# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))    # Expected output: False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function with a generator expression to check this condition. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are true, and `False` otherwise. The generator expression checks each number in the list to see if it's less than the threshold, and `all` short-circuits as soon as it encounters a number that's not less than the threshold, making this function efficient even for large lists.