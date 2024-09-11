**Below Threshold Function**
==========================

Here's a Python function that meets the requirements:

```markdown
# below_threshold.py

def below_threshold(lst: list, threshold: int) -> bool:
    """
    Return True if all numbers in the list are below the given threshold.

    Args:
    lst (list): A list of numbers.
    threshold (int): The threshold value.

    Returns:
    bool: True if all numbers in the list are below the threshold, False otherwise.

    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(num < threshold for num in lst)

# Example usage:
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
```

In this script, the `below_threshold` function uses the built-in `all()` function in combination with a generator expression to check if all numbers in the list `lst` are below the `threshold`. The function returns `True` if all numbers are below the threshold, and `False` otherwise.