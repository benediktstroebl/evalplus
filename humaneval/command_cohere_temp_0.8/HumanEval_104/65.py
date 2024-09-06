```python
def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This script provides a function `unique_digits` that takes in a list of integers (`xs`). It uses a list comprehension to filter out integers from `xs` that have no even digits. Then it sorts the resultant list in ascending order and returns it.

Here is an example of how you can use the function with the given input:
```python
print(unique_digits([15, 33, 1422, 1, 322]))
```

The function would then return:
```
[1, 15, 33]
```