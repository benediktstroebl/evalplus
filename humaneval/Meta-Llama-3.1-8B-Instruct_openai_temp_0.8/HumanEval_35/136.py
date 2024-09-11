### Max Element in List
#### Problem Statement
Find the maximum element in a given list.

#### Solution
```python
def max_element(lst: list) -> any:
    """
    Return maximum element in the list.
    
    Args:
    lst (list): Input list of elements.
    
    Returns:
    any: Maximum element in the list.
    
    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)
```

#### Explanation
This script defines a function `max_element` that takes a list `lst` as input. It uses the built-in `max` function in Python to find the maximum element in the list. If the input list is empty, it raises a `ValueError`.

You can use this function as shown in the example usage in the docstring.

#### Example Usage
```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```