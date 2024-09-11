```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.

    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold to compare with.

    Returns:
    bool: Whether all numbers in the list are below the threshold.
    """
    return all(i < threshold for i in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # True
print(below_threshold([1, 20, 4, 10], 5))   # False
```

In this script, the `below_threshold` function takes a list of numbers (`lst`) and a threshold value (`threshold`) as input. It uses the `all` function in combination with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable are `True`, and `False` otherwise. The generator expression `i < threshold for i in lst` yields `True` for each number `i` in the list if it is less than the threshold, and `False` otherwise.