### Maximum Element in a List

Below is a Python script that defines a function `max_element` to find the maximum element in a list.

```python
def max_element(l: list) -> int:
    """
    Return the maximum element in the list.

    Args:
    l (list): The list of elements.

    Returns:
    int: The maximum element in the list.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Check if the list is empty
    if not l:
        raise ValueError("List is empty")
    # Use the built-in max function to find the maximum element
    return max(l)
```

You can use this function by running the script and calling `max_element` with your list as an argument.

```python
# Example usage:
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(numbers))  # Output: 123
```