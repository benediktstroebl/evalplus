### Max Element in a List
#### Problem Statement
Find the maximum element in a given list of numbers.

#### Solution
```python
def max_element(numbers: list) -> int:
    """
    Return the maximum element in the list.

    Args:
    numbers (list): A list of numbers.

    Returns:
    int: The maximum element in the list.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(numbers)
```
This solution uses Python's built-in `max()` function to find the maximum element in the list. This function takes an iterable (like a list) as an argument and returns its maximum element.

#### Explanation
- The function `max_element` takes a list of numbers as input and returns the maximum element.
- The `return` statement uses the built-in `max` function to find the maximum element in the list.
- This solution assumes that the input list is not empty. If you want to add error checking, you could use a conditional statement to check if the list is empty and raise an exception or return a default value if it is.