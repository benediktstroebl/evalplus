```python
def below_threshold(lst: list, t: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold t.

    Args:
        lst (list): A list of numbers.
        t (int): The threshold.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(i < t for i in lst)


# Example use cases:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

This Python script defines a function `below_threshold` that checks if all elements in a given list are below a specified threshold. It uses the built-in `all` function with a generator expression to check the condition. If all elements meet the condition, the function returns `True`; otherwise, it returns `False`. The script includes example use cases to demonstrate the function's behavior.