```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list as an argument and returns a list of all positive numbers found in the input list. The function achieves this using a list comprehension, filtering out elements that are not greater than zero. 

Here's an example of using the `get_positive` function:
```python
print(get_positive([-1, 2, -4, 5, 6]))  # Expected output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Expected output: [5, 3, 2, 3, 9, 123, 1]
```

This would produce the following output:
```
[2, 5, 6]
[5, 3, 2, 3, 9, 123, 1]
```

The expected output aligns with the behavior described in the original problem statement. The function only retrieves positive numbers from the input list, ignoring any negative or zero values.