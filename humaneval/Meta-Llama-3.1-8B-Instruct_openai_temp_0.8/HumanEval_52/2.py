```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of integers
    threshold (int): The threshold value

    Returns:
    bool: True if all numbers in the list are below threshold, False otherwise
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of integers and a threshold value as input, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all` function along with a generator expression to check this condition. The example usage demonstrates how to use the function with the provided test cases.