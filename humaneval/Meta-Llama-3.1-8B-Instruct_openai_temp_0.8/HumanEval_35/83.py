```markdown
### Max Element Function

This Python function takes a list of elements as input and returns the maximum element.

#### Code
```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)
```

#### Explanation

This function uses Python's built-in `max()` function to find the maximum element in the list. The `max()` function takes an iterable as input and returns the maximum element.

#### Usage

To use this function, simply pass a list of elements as an argument, like this:
```python
result = max_element([1, 2, 3, 4, 5])
print(result)  # Output: 5
```
```