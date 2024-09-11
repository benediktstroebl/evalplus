```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    # Use all() function in combination with a generator expression to check if all numbers in the list are below the threshold
    return all(num < threshold for num in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of integers and a threshold value as input. It uses the `all()` function in combination with a generator expression to check if all numbers in the list are below the threshold. The function returns `True` if all numbers are below the threshold and `False` otherwise. The example usage at the end demonstrates how to use this function with the provided test cases.