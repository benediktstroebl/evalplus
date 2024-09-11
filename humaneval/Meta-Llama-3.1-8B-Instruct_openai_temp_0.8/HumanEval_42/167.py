Here's a Python function that accomplishes the task:
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.
    
    Args:
    l (list): A list of integers.
    
    Returns:
    list: The input list with all elements incremented by 1.
    
    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]
```
Let's break this down:

*   We define a function `incr_list` that takes a list `l` as input and returns a new list.
*   We use a list comprehension to create the new list, where each element `x` in the input list is incremented by 1 (`x + 1`).
*   We include a docstring that describes the function's purpose, input, output, and provides example use cases.

You can test this function with the examples provided in the docstring:
```python
print(incr_list([1, 2, 3]))  # [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```