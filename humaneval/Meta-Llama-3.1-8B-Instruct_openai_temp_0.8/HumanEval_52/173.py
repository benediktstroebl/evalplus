```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list are below threshold.
    
    Args:
    lst (list): A list of integers.
    threshold (int): The maximum value allowed in the list.
    
    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num <= threshold for num in lst)


# Example use cases
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script provides the function `below_threshold` which takes a list of integers `lst` and an integer `threshold` as arguments, and returns a boolean value indicating whether all numbers in the list are below the threshold. The `all` function is used with a generator expression to check each number in the list, and the `<=` operator is used to compare each number with the threshold. The script also includes example use cases to demonstrate the function's behavior.