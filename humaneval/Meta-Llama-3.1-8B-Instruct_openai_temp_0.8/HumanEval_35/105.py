### Max Element in List
#### Problem Statement
Write a Python function to find the maximum element in a given list.

#### Solution

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
```

This function uses Python's built-in `max` function, which returns the largest item in an iterable or the largest of two or more arguments. It automatically handles the case where the list is empty.