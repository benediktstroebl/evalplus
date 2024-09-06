```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers found in `l`. The function accomplishes this using a list comprehension and filtering logic based on the condition `x > 0`. 

To test this function, you can use the following sample test lists, which are replicated from the original problem description:
```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
```

These test cases illustrate how the function can be used to obtain lists of positive numbers from variously composed input lists, demonstrating its practicality and flexibility in handling such tasks.