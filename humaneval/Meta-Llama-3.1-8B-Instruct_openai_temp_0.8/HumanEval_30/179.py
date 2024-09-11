### Positive Numbers in a List
#### Filtering Positive Numbers in a Python List

Below is a simple Python script that filters a list to include only positive numbers.

```python
def get_positive(l: list):
    """Return only positive numbers in the list.

    Args:
        l (list): A list of numbers.

    Returns:
        list: A list with only positive numbers.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]

# Example usage:
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [2, 5, 6]

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
positive_numbers = get_positive(numbers)
print(positive_numbers)  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that takes a list `l` as input. It uses a list comprehension to create a new list that includes only the numbers from `l` that are greater than 0. The result is then returned by the function.