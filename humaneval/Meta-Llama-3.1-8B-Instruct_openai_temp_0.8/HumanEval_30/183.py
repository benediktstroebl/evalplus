```python
def get_positive(numbers: list) -> list:
    """Return only positive numbers in the list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        list: A list of positive numbers.
    
    Example:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Test the function
if __name__ == "__main__":
    print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
    print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```

This Python script defines a function `get_positive` that uses a list comprehension to return a new list containing only the positive numbers from the input list. The function includes docstrings for documentation and example usage. The script also includes test cases to demonstrate the function's behavior.