### Positive Numbers in List
#### Python Script

```python
def get_positive(numbers: list) -> list:
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A list of positive integers from the input list.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]


# Example usage
numbers1 = [-1, 2, -4, 5, 6]
numbers2 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]

print(get_positive(numbers1))   # Output: [2, 5, 6]
print(get_positive(numbers2))   # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that uses a list comprehension to filter out non-positive numbers from the input list. It then demonstrates the function's usage with two example lists.