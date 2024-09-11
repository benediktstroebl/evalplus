### Filter Positive Numbers from a List
```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

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
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]
```
This script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the original list. The function uses a list comprehension to filter out negative and zero numbers.

You can run this script to test the function with the provided examples. The function should return the expected output for both example lists.