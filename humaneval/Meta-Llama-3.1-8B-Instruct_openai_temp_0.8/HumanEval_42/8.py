### Increment List Elements
```python
def incr_list(l: list) -> list:
    """Return list with elements incremented by 1.

    Args:
        l (list): List of integers.

    Returns:
        list: List with elements incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in l]

# Test the function
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This Python script defines a function `incr_list` that takes a list of integers as input and returns a new list with each element incremented by 1. The function uses a list comprehension to achieve this. The script also includes example test cases to demonstrate the function's behavior.