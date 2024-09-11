```python
def max_element(lst: list) -> int:
    """Return the maximum element in the list.

    Args:
    lst (list): A list of numbers.

    Returns:
    int: The maximum element in the list.

    """
    if not lst:
        raise ValueError("List is empty.")
    return max(lst)

# Example usage
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

In this script, we define a function `max_element` that takes a list of numbers as input and returns the maximum element in the list. If the list is empty, it raises a `ValueError`. We use the built-in `max` function to find the maximum element, which makes the code concise and efficient. The example usage at the end demonstrates how to use the function with some test cases.