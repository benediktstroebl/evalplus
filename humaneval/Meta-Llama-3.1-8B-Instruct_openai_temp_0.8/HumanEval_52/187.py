```python
def below_threshold(lst: list, threshold: int) -> bool:
    """Return True if all numbers in the list lst are below threshold threshold.
    
    Args:
        lst (list): A list of integers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)


# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Expected output: True
print(below_threshold([1, 20, 4, 10], 5))   # Expected output: False
```

This script defines a function `below_threshold` that takes a list of integers `lst` and a threshold value `threshold` as input, and returns `True` if all numbers in the list are below the threshold, and `False` otherwise. The `all` function with a generator expression is used to check this condition for each number in the list. The example usage section demonstrates how to call this function with the provided test cases.