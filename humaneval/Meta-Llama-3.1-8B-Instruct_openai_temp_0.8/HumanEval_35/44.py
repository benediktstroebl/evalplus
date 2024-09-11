### Maximum Element in a List

The following Python script defines a function `max_element` that finds the maximum element in a given list.

```python
def max_element(lst: list) -> float:
    """Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        float: The maximum element in the list.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("Input list is empty")
    return max(lst)

# Example usage
if __name__ == "__main__":
    try:
        print(max_element([1, 2, 3]))  # Output: 3
        print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
        print(max_element([]))  # Raises ValueError
    except ValueError as e:
        print(f"Error: {e}")
```

This script defines a function `max_element` that takes a list of elements as input and returns the maximum element. It uses the built-in `max` function from Python's standard library to find the maximum element. If the input list is empty, it raises a `ValueError` with an appropriate message. The script also includes example usage and error handling in the `if __name__ == "__main__":` block.