```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The threshold value.
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    
    # Use the built-in all() function in combination with a generator expression
    # The generator expression checks if each number in the list is less than the threshold
    return all(num < threshold for num in lst)

# Test cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This Python script defines a function `below_threshold` which takes a list `lst` and a threshold `threshold` as input. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The function uses the built-in `all()` function in combination with a generator expression to achieve this. The test cases at the end demonstrate the function's behavior with different inputs.