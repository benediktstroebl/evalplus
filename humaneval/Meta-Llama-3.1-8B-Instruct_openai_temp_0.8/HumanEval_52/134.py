```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The maximum allowed value in the list.
    
    Returns:
    bool: Whether all numbers in the list are below the threshold.
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function in combination with a generator expression to efficiently check each number in the list. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage at the end demonstrates the function's behavior with two test cases.