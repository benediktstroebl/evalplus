```markdown
### Positive Number Filter

#### Function Description

This function filters a list of numbers and returns a new list containing only the positive numbers.

#### Code

```python
def get_positive(l: list):
    """
    Return only positive numbers in the list.

    Args:
    l (list): A list of numbers.

    Returns:
    list: A new list with only positive numbers.

    Examples:
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in l if num > 0]
```

#### Example Usage

```python
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that uses a list comprehension to filter out non-positive numbers from the input list `l`. The function returns a new list containing only the positive numbers. The example usage demonstrates how to call the function with different inputs and print the results.