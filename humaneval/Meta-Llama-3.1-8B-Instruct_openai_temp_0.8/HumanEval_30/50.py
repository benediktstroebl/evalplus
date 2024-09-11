```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.
    
    Args:
        numbers (list): A list of numbers.
    
    Returns:
        list: A list of positive numbers from the input list.
    
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Test the function
if __name__ == "__main__":
    print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
    print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that uses a list comprehension to filter out non-positive numbers from the input list. The function includes docstrings for documentation and includes example use cases. The script also has test cases at the end to demonstrate the function's usage.