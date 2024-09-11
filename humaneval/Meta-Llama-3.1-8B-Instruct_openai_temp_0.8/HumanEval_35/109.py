Here is a self-contained Python script that solves the problem:
```markdown
# Max Element in List
================================

This script defines a function `max_element` that returns the maximum element in a given list.

```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
    - l (list): The input list.

    Returns:
    - The maximum element in the list.

    Examples:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)

# Test the function
print(max_element([1, 2, 3]))  # Expected output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: 123
```

You can save this script to a file (e.g., `max_element.py`) and run it using Python (e.g., `python max_element.py`). The script will print the maximum element in the list `l` for the two test cases.

Note: The `max` function is a built-in Python function that returns the largest item in an iterable or the largest of two or more arguments. In this script, we use it to find the maximum element in the input list `l`.