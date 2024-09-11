```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below the threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers are below the threshold, False otherwise.
    """
    return all(i < threshold for i in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

In this script, the `below_threshold` function uses the built-in `all` function along with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements of the iterable are true, and `False` otherwise.