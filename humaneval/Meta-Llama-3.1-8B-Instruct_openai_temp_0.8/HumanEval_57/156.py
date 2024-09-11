```python
def monotonic(lst):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        lst (list): A list of elements to check.

    Returns:
        bool: True if list is monotonically increasing or decreasing, False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) or all(lst[i] >= lst[i+1] for i in range(len(lst)-1))


# Example usage:
if __name__ == "__main__":
    print(monotonic([1, 2, 4, 20]))  # Expected output: True
    print(monotonic([1, 20, 4, 10]))  # Expected output: False
    print(monotonic([4, 1, 0, -10]))  # Expected output: True
```

In this script, the function `monotonic` checks if the elements in the input list are monotonically increasing or decreasing. It does this by checking two conditions:

1. The list is monotonically increasing, which means that each element is less than or equal to the next element.
2. The list is monotonically decreasing, which means that each element is greater than or equal to the next element.

The `all` function is used to check if all elements in the list satisfy the conditions. If any element does not satisfy the conditions, the function returns `False`. If all elements satisfy the conditions, the function returns `True`.