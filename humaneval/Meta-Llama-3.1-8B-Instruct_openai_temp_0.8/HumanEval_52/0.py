```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the threshold.
    
    Args:
        numbers (list): A list of numbers to check.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

In this script, we define a function `below_threshold` that takes a list of numbers and a threshold value. It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable are true, and `False` otherwise.