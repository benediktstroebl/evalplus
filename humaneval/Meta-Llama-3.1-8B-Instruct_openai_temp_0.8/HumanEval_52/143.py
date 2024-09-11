```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The maximum allowed value.
    
    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(i < threshold for i in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage at the end demonstrates how to use the function.