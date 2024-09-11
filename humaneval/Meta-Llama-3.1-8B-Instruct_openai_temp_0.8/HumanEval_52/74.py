```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    
    Example:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that checks whether all numbers in a given list are below a specified threshold. It uses the built-in `all` function with a generator expression to efficiently check the condition for all numbers in the list. The script then includes two example test cases to demonstrate the function's behavior.