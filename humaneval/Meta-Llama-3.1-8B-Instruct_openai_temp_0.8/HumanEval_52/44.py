```python
def below_threshold(numbers: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the threshold.

    Args:
        numbers (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < threshold for num in numbers)


# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value. It uses the built-in `all` function with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. If any number is not below the threshold, `all` returns `False`.