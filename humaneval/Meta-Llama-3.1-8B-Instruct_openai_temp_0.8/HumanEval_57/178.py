Here's a Python function that implements the `monotonic` function:
```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of elements to check.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    # Check if the list is monotonically increasing or decreasing
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or \
           all(lst[i] >= lst[i+1] for i in range(len(lst)-1))


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected output: True
print(monotonic([1, 20, 4, 10]))  # Expected output: False
print(monotonic([4, 1, 0, -10]))  # Expected output: True
```
This script uses a list comprehension to generate two conditions: one for monotonically increasing sequences (`lst[i] <= lst[i+1]`) and one for monotonically decreasing sequences (`lst[i] >= lst[i+1]`). The `all()` function checks if all elements in the list satisfy these conditions. The `or` operator returns `True` if either of the conditions is met.