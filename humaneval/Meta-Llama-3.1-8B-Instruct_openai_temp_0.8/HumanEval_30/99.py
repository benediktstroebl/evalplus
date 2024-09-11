```python
def get_positive(numbers: list) -> list:
    """
    Returns a list of positive numbers from the input list.
    
    Args:
    numbers: A list of integers.
    
    Returns:
    A list of positive integers from the input list.
    
    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example usage:
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that takes a list of numbers and returns a new list containing only the positive numbers from the original list. The function uses a list comprehension to filter out negative numbers, and returns the resulting list. The example usage at the end demonstrates how to call the function with specific input lists and print the output.