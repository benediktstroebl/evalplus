```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the threshold.

    Args:
        lst (list): A list of numbers.
        threshold (int): The maximum value allowed in the list.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i <= threshold for i in lst)


# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Should print: True
print(below_threshold([1, 20, 4, 10], 5))   # Should print: False
```

This script defines a function `below_threshold` that checks if all numbers in a given list are below a specified threshold. The function uses the built-in `all` function with a generator expression to check the condition for each number in the list. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`.