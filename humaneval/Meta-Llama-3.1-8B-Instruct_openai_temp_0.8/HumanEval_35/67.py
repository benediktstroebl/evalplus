### Maximum Element in List
The following Python script defines a function `max_element` that returns the maximum element from a given list.

```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of numbers.

    Returns:
        int or float: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)

# Example usage
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(numbers))  # Output: 123
```

### Explanation

*   The function `max_element` takes a list of numbers `lst` as input and returns its maximum element.
*   The `max` function in Python is used to find the largest item in an iterable or the largest of two or more arguments.
*   The script includes example usage of the `max_element` function with a list of numbers.
*   Docstrings are used to provide documentation for the function, including its arguments, return value, and examples of usage.