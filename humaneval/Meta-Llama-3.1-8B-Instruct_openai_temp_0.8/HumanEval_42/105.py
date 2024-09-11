### Increment List Elements
#### Problem Statement
Create a Python function `incr_list` that increments each element in a given list by 1.

#### Solution
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list of numbers.

    Returns:
        list: List with elements incremented by 1.

    Example:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # Use list comprehension to create a new list with incremented elements
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines a function `incr_list` that takes a list of numbers as input, creates a new list with incremented elements using list comprehension, and returns the new list. The test cases demonstrate the function's usage and expected output.