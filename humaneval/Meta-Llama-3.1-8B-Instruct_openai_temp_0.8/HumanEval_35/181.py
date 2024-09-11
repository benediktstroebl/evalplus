Here's a simple Python function that implements the `max_element` function:
```markdown
### Max Element Function

#### Function Definition
```python
def max_element(lst: list) -> int:
    """
    Return the maximum element in the list.

    Args:
    lst (list): A list of integers.

    Returns:
    int: The maximum element in the list.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("List cannot be empty")
    return max(lst)
```

#### Example Usage
```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```
This function uses the built-in `max` function in Python to find the maximum element in the list. It first checks if the list is empty and raises a `ValueError` in that case. Otherwise, it returns the maximum element.