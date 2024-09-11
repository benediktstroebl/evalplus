```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A new list with elements incremented by 1.
    """
    return [x + 1 for x in lst]

# Example usage
print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This Python script defines a function `incr_list` that uses a list comprehension to create a new list where each element is incremented by 1. The original list remains unchanged. The function includes type hints for the input list and return value, as well as a docstring that describes the function's behavior and provides an example of usage.