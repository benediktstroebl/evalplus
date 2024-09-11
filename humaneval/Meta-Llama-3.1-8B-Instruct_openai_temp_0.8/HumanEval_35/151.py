```python
def max_element(lst: list):
    """
    Return maximum element in the input list.

    Args:
    lst (list): A list of elements.

    Returns:
    The maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(lst)

# Example usage
numbers = [1, 2, 3, 4, 5]
print(max_element(numbers))  # Output: 5
```

In this script, we use the built-in `max()` function to find the maximum element in the list. This function takes an iterable as an argument and returns the maximum item. The example usage demonstrates how to use the function with a list of numbers.