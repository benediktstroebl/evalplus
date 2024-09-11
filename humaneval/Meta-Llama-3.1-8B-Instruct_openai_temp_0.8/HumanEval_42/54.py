```markdown
### Increment List Function
#### Python Script

```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        lst (list): Input list of numbers.

    Returns:
        list: List with elements incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [num + 1 for num in lst]


# Example usage:
numbers = [1, 2, 3]
incremented_numbers = incr_list(numbers)
print(f"Incremented list: {incremented_numbers}")

numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
incremented_numbers = incr_list(numbers)
print(f"Incremented list: {incremented_numbers}")
```

This Python script defines a function `incr_list` that takes a list of numbers as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to create the new list.

The script includes docstrings to provide documentation for the function and example usage to demonstrate its application. The docstring includes explanations of the function's parameters, return value, and usage examples. 

The example usage shows how to call the `incr_list` function with two different lists of numbers and print the resulting incremented lists.