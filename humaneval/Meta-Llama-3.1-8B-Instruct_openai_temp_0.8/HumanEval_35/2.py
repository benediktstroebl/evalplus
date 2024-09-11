### Maximum Element in List
#### Problem Statement
Given a list of numbers, return the maximum element in the list.

#### Solution
```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): A list of numbers.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)
```
In this solution, we use the built-in `max()` function in Python, which returns the largest item in an iterable or the largest of two or more arguments.

You can also solve this problem manually by iterating over the list and keeping track of the maximum element:
```python
def max_element_manual(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): A list of numbers.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element_manual([1, 2, 3])
        3
        >>> max_element_manual([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    max_val = l[0]
    for num in l:
        if num > max_val:
            max_val = num
    return max_val
```
However, the built-in `max()` function is generally more efficient and Pythonic.