### Monotonic List Checker
#### Description
This script checks if a given list is either monotonically increasing or decreasing.

#### Code
```python
def monotonic(lst: list):
    """Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

    Returns:
        bool: True if list is monotonically increasing or decreasing, False otherwise.

    Example:
        >>> monotonic([1, 2, 4, 20])
        True
        >>> monotonic([1, 20, 4, 10])
        False
        >>> monotonic([4, 1, 0, -10])
        True
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1)) or \
           all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))


# Example usage:
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```
#### Explanation
This script uses a generator expression within the built-in `all()` function to check whether the list is monotonically increasing or decreasing.

The `all()` function returns `True` if all elements of the generator expression are true. The generator expression checks each pair of adjacent elements in the list.

For the list to be monotonically increasing, each pair of adjacent elements must satisfy the condition `lst[i] <= lst[i + 1]`. Therefore, we use `all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))`.

For the list to be monotonically decreasing, each pair of adjacent elements must satisfy the condition `lst[i] >= lst[i + 1]`. Therefore, we use `all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))`.

If either of these conditions is met, the function returns `True`. Otherwise, it returns `False`.