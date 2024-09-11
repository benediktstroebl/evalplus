### Max Element in a List

The following Python script defines a function `max_element` that returns the maximum element in a given list.

```markdown
### max_element.py

```python
def max_element(l: list) -> int:
    """
    Return maximum element in the list.

    Args:
        l (list): A list of integers.

    Returns:
        int: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)
```

### Usage:

```python
if __name__ == "__main__":
    # Test the function
    print(max_element([1, 2, 3]))  # Output: 3
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

### Explanation:

The `max_element` function uses Python's built-in `max` function to find the maximum element in the given list. This function iterates over all elements in the list, comparing them with each other to find the largest one. If the list is empty, it raises a `ValueError`.

This function has a time complexity of O(n), where n is the number of elements in the list, because it potentially needs to examine every element in the list once. The space complexity is O(1), as it does not need to allocate any additional space that scales with the input size.

This script can be saved as `max_element.py` and run using Python (e.g., `python max_element.py`). The example usage in the `if __name__ == "__main__":` block demonstrates how to use the `max_element` function.