```python
def below_threshold(lst: list, t: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold t.

    Args:
        lst (list): A list of numbers.
        t (int): The threshold value.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(num < t for num in lst)


# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that checks if all elements in a given list are below a specified threshold. The function uses the built-in `all` function with a generator expression to check the condition for each number in the list. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage demonstrates how to use the `below_threshold` function with different inputs.