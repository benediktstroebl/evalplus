```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    
    Args:
        lst (list): A list of numbers
        threshold (int): The threshold value
    
    Returns:
        bool: True if all numbers are below threshold, False otherwise
    """
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function in combination with a generator expression to check each number in the list. The `all` function returns `True` if all elements in the iterable are true. If at least one element is false, `all` returns `False`. The `all` function is a more concise and readable way to check this condition than using a for loop.