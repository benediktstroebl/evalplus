Here's a Python script that defines the `max_element` function to find the maximum element in a list:
```markdown
### Find Maximum Element in a List

This script defines a function `max_element` to find the maximum element in a list.

#### Code

```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(lst)

# Test the function
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

#### Explanation

The `max_element` function uses the built-in `max` function in Python, which returns the largest item in an iterable (such as a list or tuple).

In this script, we define a function `max_element` with a single argument `lst`, which is a list of elements. The function returns the maximum element in the list.

We also include examples of how to use the function with different lists. The `print` statements at the end of the script test the function with the provided examples.

This script provides a simple and efficient solution to find the maximum element in a list.