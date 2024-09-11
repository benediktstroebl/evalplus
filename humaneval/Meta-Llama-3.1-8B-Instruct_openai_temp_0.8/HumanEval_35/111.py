### Maximum Element in List
#### Problem Description
This Python script defines a function `max_element` that takes a list as input and returns its maximum element.

#### Code
```python
def max_element(lst: list) -> int:
    """Return maximum element in the list.

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
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

# Example usage
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(numbers))  # Output: 123
```
#### Explanation
- The function `max_element` takes a list `lst` as input and checks if it's empty. If it is, a `ValueError` is raised.
- If the list is not empty, the built-in `max` function is used to find and return the maximum element.
- The script includes example usage of the `max_element` function with a list of numbers.