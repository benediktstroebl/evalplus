### Python Script to Get Positive Numbers in a List

```python
def get_positive(numbers: list) -> list:
    """
    Return a list of only positive numbers in the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of positive integers.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example usage:
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]
```

This script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. The function uses a list comprehension to achieve this in a concise and efficient manner. The example usage demonstrates how to use the function with a sample list of numbers.