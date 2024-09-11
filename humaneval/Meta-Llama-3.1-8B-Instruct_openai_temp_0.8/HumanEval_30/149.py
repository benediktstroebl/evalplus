```python
def get_positive(lst: list):
    """
    Return only positive numbers in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        list: A new list containing only the positive numbers from the input list.
    """
    return [num for num in lst if num > 0]

# Test cases
print(get_positive([-1, 2, -4, 5, 6]))  # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # [5, 3, 2, 3, 9, 123, 1]
```

This script defines a function `get_positive` that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. The function uses a list comprehension to achieve this.

The list comprehension iterates over each number `num` in the input list `lst`. If the number is greater than 0, it is included in the new list.

The script also includes two test cases to verify that the function works as expected.