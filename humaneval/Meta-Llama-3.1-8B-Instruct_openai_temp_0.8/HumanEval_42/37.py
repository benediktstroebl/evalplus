### Increment List Elements

Below is a Python script that includes the function `incr_list` to increment each element in a given list by 1.

```markdown
### Code

```python
def incr_list(lst: list) -> list:
    """
    Return list with elements incremented by 1.

    Examples:
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [i + 1 for i in lst]


# Example usage:
numbers = [1, 2, 3]
print(incr_list(numbers))  # Output: [2, 3, 4]

numbers = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(incr_list(numbers))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

### Explanation

The `incr_list` function uses a list comprehension to create a new list where each element is the original element incremented by 1. This approach is more memory-efficient than modifying the original list in-place, as it avoids the overhead of shifting elements when inserting a new value.

### Advice

This script helps demonstrate how list comprehensions can be used for simple transformations on lists in Python.