```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in lst are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as input. It uses the `all` function with a generator expression to check if all numbers in the list are below the threshold. The function returns `True` if all numbers are below the threshold and `False` otherwise. The example usage demonstrates how to use the function with the provided test cases.