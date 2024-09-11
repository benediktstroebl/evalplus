### Maximum Element in a List
#### Problem Description
Find the maximum element in a given list.

#### Solution
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
    if not lst:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(lst)  # Return the maximum element in the list
```

#### Explanation
This script defines a function `max_element` that takes a list `lst` as input and returns its maximum element. The function uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments.

If the input list is empty, the function raises a `ValueError` with the message "List is empty".

#### Example Use Cases
```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Output: ValueError: List is empty
```