```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.

    Example:
        >>> below_threshold([1, 2, 4, 10], 100)
        True
        >>> below_threshold([1, 20, 4, 10], 5)
        False
    """
    return all(num < threshold for num in lst)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```
In this script, we define a function `below_threshold` that takes a list `lst` and an integer `threshold` as arguments. It uses the `all()` function along with a generator expression to check if all numbers in the list are less than the threshold. If all numbers are below the threshold, it returns `True`; otherwise, it returns `False`. The function is then tested with the provided examples.