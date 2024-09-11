```python
def below_threshold(lst: list, threshold: int):
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(x < threshold for x in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold value. It uses the built-in `all` function with a generator expression to check this condition. The example usage at the end demonstrates how to use this function.