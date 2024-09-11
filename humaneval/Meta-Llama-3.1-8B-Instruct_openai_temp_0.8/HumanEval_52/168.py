```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The maximum allowed value.
    
    Returns:
    bool: True if all numbers are below threshold, False otherwise.
    """
    
    # Use the built-in all() function in combination with a generator expression
    # to check if all numbers in the list are below the threshold
    return all(i < threshold for i in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input, and returns a boolean indicating whether all numbers in the list are below the threshold. The function uses the `all()` function in combination with a generator expression to check this condition. The script also includes example usage of the function.