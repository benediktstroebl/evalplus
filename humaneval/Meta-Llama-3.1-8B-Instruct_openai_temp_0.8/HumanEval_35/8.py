### Maximum Element in a List
#### Problem Statement
Given a list of elements, return the maximum element.

#### Solution
```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.

    Args:
    lst (list): A list of elements.

    Returns:
    int: The maximum element in the list.

    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(lst)
```
This solution utilizes Python's built-in `max` function, which returns the largest item in an iterable or the largest of two or more arguments.

#### Notes
- The function `max_element` takes a list `lst` as input and returns the maximum element.
- The `max` function is used to find the maximum element in the list.
- The function includes docstrings to provide documentation and example usage.
- The type hints are used to specify the input and output types of the function.