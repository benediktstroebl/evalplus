### Maximum Element in a List
#### Problem Statement
Write a Python function to find the maximum element in a given list.

#### Solution
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
    if not lst:
        raise ValueError("List is empty")
    return max(lst)
```
#### Explanation
This function uses Python's built-in `max()` function to find the maximum element in the list. It also checks if the list is empty and raises a `ValueError` in that case.

#### Example Use Cases
```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Raises ValueError
```