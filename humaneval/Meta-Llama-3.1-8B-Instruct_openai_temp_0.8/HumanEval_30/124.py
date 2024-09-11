```python
def get_positive(numbers: list):
    """
    Return only positive numbers in the list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A list of positive numbers.
    """
    return [num for num in numbers if num > 0]


# Example use cases
if __name__ == "__main__":
    print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]
    print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that uses list comprehension to return a list of numbers that are greater than 0. The function is then tested with the example use cases provided in the docstring.