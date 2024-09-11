```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold number.
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    
    Example:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(i < threshold for i in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))    # False
```

This script defines the `below_threshold` function which checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function with a generator expression to check each number in the list. If any number is not below the threshold, the `all` function returns False. Otherwise, it returns True. The script also includes test cases to demonstrate the function's usage.