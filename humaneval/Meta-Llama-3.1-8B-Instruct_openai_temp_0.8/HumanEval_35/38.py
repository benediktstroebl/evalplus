### Maximum Element in a List
#### Python Script

```python
def max_element(l: list):
    """Return maximum element in the list.

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
    return max(l)

# Example usage
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(numbers))  # Output: 123
```

In this script, we use the built-in `max()` function in Python to find the maximum element in the list. This function takes an iterable (like a list or tuple) as an argument and returns the largest item. If the list is empty, it raises a `ValueError`. However, we can also add error handling to our function to make it more robust. 

Here's an updated version with error handling:

```python
def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        The maximum element in the list.

    Raises:
        ValueError: If the list is empty.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:
        raise ValueError("List is empty")
    return max(l)
```