### Increment List Function

Here's a Python function that increments each element in a list by 1:
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list with integers.

    Returns:
        list: List with each element incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]
```

### Usage Example

You can use this function as follows:
```python
numbers = [1, 2, 3]
incremented_numbers = incr_list(numbers)
print(incremented_numbers)  # Output: [2, 3, 4]

numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
incremented_numbers = incr_list(numbers)
print(incremented_numbers)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This function uses a list comprehension, which is a concise way to create a new list by applying an operation to each element of an existing list. In this case, the operation is simply adding 1 to each element.