```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold to compare with.
    
    Returns:
    bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold as input, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all` function in combination with a generator expression to check this condition. The example usage at the end demonstrates how to call this function with different inputs.