```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of numbers and a threshold value as arguments. The function uses the built-in `all` function along with a generator expression to check if all numbers in the list are below the threshold. The `all` function returns `True` if all elements in the iterable are true, and `False` otherwise. If the list is empty, the function will return `True` since there are no numbers below the threshold that don't meet the condition.