```markdown
### Maximum Element in a List

#### Problem Statement
Write a Python function `max_element` that takes a list of integers as input and returns the maximum element in the list.

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
    return max(lst)
```

#### Explanation
This solution uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments. The list is passed as an argument to the `max` function, and the maximum element is returned.

#### Usage
To use this function, simply import it into your code and call it with a list of integers as an argument. For example:

```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

Note: This solution assumes that the input list is not empty. If the list is empty, the `max` function will raise a `ValueError`. Depending on the requirements of your program, you may want to add error checking to handle this case.