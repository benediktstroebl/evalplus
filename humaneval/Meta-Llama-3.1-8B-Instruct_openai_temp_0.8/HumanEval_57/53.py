```markdown
### Monotonic List Validator
#### Python Function to Check if List Elements are Monotonically Increasing or Decreasing

```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of integers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.

    Examples:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return is_increasing or is_decreasing
```

### Example Usage
```python
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
This script defines a function `monotonic` that takes a list of integers as input and returns `True` if the list is monotonically increasing or decreasing, and `False` otherwise. The function uses list comprehensions to check if the list is increasing or decreasing. The example usage demonstrates how to use the function with different inputs.