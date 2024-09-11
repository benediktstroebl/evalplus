```python
def get_positive(numbers: list) -> list:
    """
    Return a list of only positive numbers from the input list.

    Args:
        numbers: A list of integers.

    Returns:
        A list of positive integers.

    Examples:
        >>> get_positive([-1, 2, -4, 5, 6])
        [2, 5, 6]
        >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        [5, 3, 2, 3, 9, 123, 1]
    """
    return [num for num in numbers if num > 0]
```

You can save this script to a file, for example `positive_numbers.py`, and then run it using Python:

```bash
python positive_numbers.py
```

This will execute the code and print the result to the console. You can also use a Python interpreter to execute this code line by line.