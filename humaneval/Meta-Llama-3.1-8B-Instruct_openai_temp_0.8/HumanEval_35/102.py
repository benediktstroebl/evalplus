### Maximum Element in List
#### Problem Description
Given a list of elements, return the maximum element.

#### Solution
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
    # Check if the list is empty
    if not lst:
        raise ValueError("List is empty")
    
    # Use built-in max function to find the maximum element
    return max(lst)
```
This script defines a function `max_element` that takes a list `lst` as input and returns the maximum element in the list. If the input list is empty, it raises a ValueError. It uses the built-in `max` function to find the maximum element, which is more efficient and Pythonic than implementing a custom solution.