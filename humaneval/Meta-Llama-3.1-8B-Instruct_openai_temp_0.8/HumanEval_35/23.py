### Maximum Element in a List
#### Problem Statement
Write a Python function `max_element` that takes a list as input and returns the maximum element.

#### Solution
```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): Input list of elements.

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
The `max_element` function takes a list `l` as input and returns the maximum element. It first checks if the list is empty, raising a `ValueError` if it is. Otherwise, it uses the built-in `max` function to find the maximum element in the list.

#### Example Use Cases

```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([]))  # Raises ValueError: List is empty
```