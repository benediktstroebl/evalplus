Here's the self-contained Python script that solves the problem:

```markdown
### Positive Numbers in a List

This script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers.

```python
def get_positive(lst: list):
    """
    Return only positive numbers in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        list: A list of positive numbers.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in lst if num > 0]


# Example usage:
numbers = [-1, 2, -4, 5, 6]
positive_numbers = get_positive(numbers)
print("Positive numbers:", positive_numbers)

numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
positive_numbers = get_positive(numbers)
print("Positive numbers:", positive_numbers)
```

You can save this script to a file (e.g., `positive_numbers.py`) and run it using Python (e.g., `python positive_numbers.py`) to see the example usage in action.
```