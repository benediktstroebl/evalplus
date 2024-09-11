```python
def get_positive(numbers: list):
    """Return only positive numbers in the list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        list: A list of positive numbers.
    
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example usage:
numbers = [-1, 2, -4, 5, 6]
print(get_positive(numbers))  # Output: [2, 5, 6]

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(get_positive(numbers))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that takes a list of numbers and returns a new list containing only the positive numbers. The function uses a list comprehension to filter out non-positive numbers. The example usage demonstrates how to call the function with different inputs and print the results.