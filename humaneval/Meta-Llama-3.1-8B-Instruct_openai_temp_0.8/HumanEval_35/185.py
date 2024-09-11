### Python Script: Maximum Element in List

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
    # Check if the list is empty
    if not lst:
        raise ValueError("List cannot be empty")
    # Return the maximum element using built-in max function
    return max(lst)


# Example usage:
if __name__ == "__main__":
    print(max_element([1, 2, 3]))  # Output: 3
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
    try:
        print(max_element([]))  # Raises ValueError
    except ValueError as e:
        print(e)  # Output: List cannot be empty
```

This Python script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. It uses the built-in `max` function to find the maximum element, which is more efficient than iterating through the list. The script also includes example usage and error handling for an empty list.