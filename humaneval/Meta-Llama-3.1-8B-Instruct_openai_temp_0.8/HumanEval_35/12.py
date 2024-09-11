### Maximum Element in a List
#### Problem Statement
Given a list of numbers, return the maximum element in the list.

#### Solution
```python
def max_element(l: list) -> int:
    """Return maximum element in the list.
    
    Args:
        l (list): A list of numbers.
    
    Returns:
        int: The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)
```
This script uses the built-in `max()` function in Python to find the maximum element in the list. The `max()` function takes an iterable (like a list) as an argument and returns the maximum item in that iterable. 

You can use this script by calling the `max_element()` function with a list of numbers as an argument, and it will return the maximum element in the list.