```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): Input list of integers

    Returns:
        list: Input list with each element incremented by 1
    """
    return [x + 1 for x in l]

# Example usage:
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list of integers as input and returns a new list where each element has been incremented by 1. It uses a list comprehension to create the new list, which is a concise and efficient way to perform this operation. The example usage at the end demonstrates how to use the function with the example inputs provided in the problem statement.