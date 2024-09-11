```python
def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the threshold.
    
    Args:
        lst (list): A list of numbers.
        threshold (int): The threshold value.
    
    Returns:
        bool: True if all numbers in the list are below the threshold, False otherwise.
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

This Python script defines a function `below_threshold` that takes a list `lst` and an integer `threshold` as input and returns a boolean indicating whether all numbers in the list are below the threshold. The `all` function with a generator expression is used to check if all numbers in the list meet the condition. If all numbers are below the threshold, the function returns `True`; otherwise, it returns `False`. The example usage demonstrates the function's behavior with two test cases.