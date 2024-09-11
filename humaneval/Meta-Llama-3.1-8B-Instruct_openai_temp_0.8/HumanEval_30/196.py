### Positive Numbers in a List
#### Solution

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
```

#### Explanation

This script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers. The function uses a list comprehension to filter out non-positive numbers.

#### Example Usage

```python
print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```