```python
def monotonic(lst: list) -> bool:
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): The input list to check.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    is_decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))
    
    return is_increasing or is_decreasing


# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

In this script, the `monotonic` function takes a list as input and uses two generator expressions to check if the list is monotonically increasing (`is_increasing`) or decreasing (`is_decreasing`). The `all` function checks if all elements in the list satisfy the condition. The function then returns `True` if either condition is met, and `False` otherwise.