```python
def get_positive(lst: list):
    """
    Return only positive numbers in the list.
    
    Args:
        lst (list): The input list that may contain both positive and negative numbers.
    
    Returns:
        list: A new list containing only the positive numbers from the input list.
    
    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in lst if num > 0]

# Testing the function
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that uses a list comprehension to filter out negative numbers from the input list. The function takes a list as input and returns a new list containing only the positive numbers. The `if num > 0` condition in the list comprehension filters out numbers that are not greater than 0, effectively keeping only the positive numbers. The function's docstring provides a description of its behavior, its input and output parameters, and several examples of usage.