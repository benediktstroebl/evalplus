```python
def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.
    
    A list is monotonically increasing if each element is greater than or equal to the previous one.
    A list is monotonically decreasing if each element is less than or equal to the previous one.

    Args:
        l (list): A list of elements.

    Returns:
        bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))


# Test cases
print(monotonic([1, 2, 4, 20]))  # Expected: True
print(monotonic([1, 20, 4, 10]))  # Expected: False
print(monotonic([4, 1, 0, -10]))  # Expected: True
```

This script defines a function `monotonic` that checks if the elements in a list are monotonically increasing or decreasing. The function uses the `all` function along with generator expressions to check if all elements in the list are related in a particular way (either increasing or decreasing). The `zip` function is used to iterate over the elements of the list in pairs. The test cases at the end of the script demonstrate the function's behavior with different inputs.