### Positive Number Filter
```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        numbers: A list of integers.

    Returns:
        A list of positive integers from the input list.

    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]

# Example usage:
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [5, 3, 2, 3, 9, 123, 1]
```
This script defines a function `get_positive` that takes a list of integers as input and returns a new list containing only the positive numbers from the input list. It uses a list comprehension to achieve this in a concise and efficient manner. The example usage demonstrates how to call the function with a sample list of numbers.