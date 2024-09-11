```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.

    Returns:
        bool: True if all numbers in the list are below threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

In this code:

- The function `below_threshold` takes a list and a threshold value as parameters.
- It uses the built-in `all` function in combination with a generator expression to check if all numbers in the list are below the threshold.
- The `all` function will return `True` if all numbers in the list satisfy the condition `num < threshold` (for `num` in `lst`), and `False` otherwise.
- The code includes two test cases to demonstrate the function's behavior.