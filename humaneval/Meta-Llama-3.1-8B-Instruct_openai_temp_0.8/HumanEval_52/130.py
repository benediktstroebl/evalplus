```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Returns: True
print(below_threshold([1, 20, 4, 10], 5))   # Returns: False
```

This Python script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It returns `True` if all numbers in the list are below the threshold and `False` otherwise. The `all` function with a generator expression is used to check if all numbers in the list meet the condition. The example usage at the end demonstrates how to use this function with different inputs.