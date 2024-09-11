Here's a simple Python function that uses a list comprehension to increment each element in the list by 1:

```markdown
```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
    l (list): A list of numbers.

    Returns:
    list: A list with each element incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Test the function
print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This function works by using a list comprehension to iterate over each element `x` in the input list `l`. For each element, it adds 1 to `x` and includes the result in the output list. The function then returns this new list.