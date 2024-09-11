```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        lst (list): The input list.

    Returns:
        list: The list with all elements incremented by 1.
    """
    return [i + 1 for i in lst]

# Example usage
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This script defines a function `incr_list` that takes a list of integers as input and returns a new list with all elements incremented by 1. The function uses a list comprehension to achieve this in a concise and efficient manner. The example usage at the end demonstrates how to use the function with the provided test cases.