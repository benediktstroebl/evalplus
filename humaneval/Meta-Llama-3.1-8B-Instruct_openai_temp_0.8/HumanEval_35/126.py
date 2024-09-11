```markdown
### max_element Function

This Python script defines a function `max_element` that takes a list as input and returns the maximum element in the list.

```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:  # Check if the list is empty
        raise ValueError("Cannot find maximum element in an empty list")
    return max(l)


# Example usage:
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(numbers))  # Output: 123
```

### Explanation:

*   The `max_element` function takes a list `l` as input and returns the maximum element using the built-in `max` function.
*   It checks if the list is empty and raises a `ValueError` if so, as finding the maximum element in an empty list is undefined.
*   The example usage demonstrates how to use the `max_element` function with a sample list of numbers.