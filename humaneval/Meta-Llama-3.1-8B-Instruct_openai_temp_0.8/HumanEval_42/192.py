### Increment List Elements
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): List of integers

    Returns:
        list: List with elements incremented by 1

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]

# Example usage:
numbers = [1, 2, 3]
print(incr_list(numbers))  # Output: [2, 3, 4]

numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(incr_list(numbers))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script uses a list comprehension to increment each element in the input list by 1. The `i + 1 for i in l` expression iterates over each element `i` in the list `l` and adds 1 to it. The result is a new list with the incremented elements.