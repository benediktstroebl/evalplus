### Maximum Element in a List
#### Problem Statement
Find the maximum element in a given list.

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
    # Use the built-in max function to find the maximum element
    return max(l)
```

#### Explanation
This solution utilizes Python's built-in `max` function, which returns the largest item in an iterable or the largest of two or more arguments.

#### Example Use Cases

```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
print(max_element([-10, -20, -30]))  # Output: -10
```