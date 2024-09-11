```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below the threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test the function
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this script, I've used Python 3.5+ style type hints for clarity. The `all()` function returns True if all elements in an iterable (in this case, a generator expression) are True. If at least one element is False, `all()` returns False. This makes the code easy to read and understand.