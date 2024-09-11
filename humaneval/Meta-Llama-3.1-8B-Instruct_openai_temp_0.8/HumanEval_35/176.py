```markdown
### Solution
```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): Input list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)
```

### Explanation
This solution uses Python's built-in `max()` function to find the maximum element in the list. The `max()` function takes an iterable as an argument and returns the largest item in that iterable.

### Example Usage
```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```

### Time Complexity
The time complexity of this solution is O(n), where n is the number of elements in the list. This is because the `max()` function needs to iterate over the entire list to find the maximum element.