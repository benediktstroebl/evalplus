### Maximum Element in List
#### Problem Statement

Write a Python function `max_element` that takes a list `l` as input and returns the maximum element in the list.

#### Solution

```python
def max_element(l: list):
    """
    Return maximum element in the list.

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
    # Check if the list is empty
    if not l:
        raise ValueError("List is empty")

    # Use built-in max function to find the maximum element
    return max(l)
```

#### Explanation

This function uses the built-in `max` function provided by Python to find the maximum element in the list. It first checks if the list is empty and raises a `ValueError` if it is. Otherwise, it returns the maximum element.

You can use this function as shown in the examples in the docstring.