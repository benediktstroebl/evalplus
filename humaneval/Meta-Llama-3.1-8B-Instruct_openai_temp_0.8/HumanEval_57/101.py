```python
def monotonic(lst: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of numbers.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
    is_decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst)-1))

    return is_increasing or is_decreasing

# Example use cases
if __name__ == "__main__":
    print(monotonic([1, 2, 4, 20]))  # True
    print(monotonic([1, 20, 4, 10]))  # False
    print(monotonic([4, 1, 0, -10]))  # True
```

This script defines a function `monotonic` that checks if the elements in a given list are monotonically increasing or decreasing. It does this by using list comprehensions to check if all pairs of consecutive elements satisfy the monotonic condition. If either the increasing or decreasing condition is met, the function returns `True`, otherwise it returns `False`.