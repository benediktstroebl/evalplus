```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 3, 2, 1]))  # False
print(monotonic([1, 1, 1, 1]))  # True
```

This script defines a function `monotonic` that takes a list as input and returns `True` if its elements are monotonically increasing or decreasing. It uses the `all` function and generator expressions to check if all pairs of adjacent elements in the list satisfy the condition of being either non-decreasing or non-increasing. The `zip(l, l[1:])` expression pairs each element in the list with the next element. The `all` function returns `True` if all elements of the given iterable are true. 

The test cases demonstrate the function's behavior with different input lists.