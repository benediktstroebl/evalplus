```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.

    Args:
        l (list): A list of elements to check.

    Returns:
        bool: True if the list elements are monotonically increasing or decreasing, False otherwise.
    """
    is_increasing = all(l[i] <= l[i+1] for i in range(len(l)-1))
    is_decreasing = all(l[i] >= l[i+1] for i in range(len(l)-1))
    return is_increasing or is_decreasing

print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
```

This Python script defines a function `monotonic` that takes a list of elements as an input and returns `True` if the elements are monotonically increasing or decreasing, and `False` otherwise. The script then demonstrates the function's usage with the provided test cases. The function uses the `all` function in combination with a generator expression to check if the list elements are in a monotonically increasing or decreasing order.