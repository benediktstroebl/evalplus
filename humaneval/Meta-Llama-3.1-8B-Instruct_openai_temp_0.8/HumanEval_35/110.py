### Maximum Element in a List
### ==========================

The following Python function finds the maximum element in a given list.

```python
def max_element(lst: list) -> any:
    """Return maximum element in the list.
    
    Args:
        lst (list): A list of elements.
    
    Returns:
        any: The maximum element in the list.
    
    Example:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(lst)
```

### Explanation

* We define a function `max_element` that takes a list `lst` as input and returns the maximum element.
* Inside the function, we first check if the list is empty. If it is, we raise a `ValueError` because there is no maximum element in an empty list.
* Otherwise, we return the maximum element using the built-in `max` function.

### Example Use Cases

```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Raises ValueError
```