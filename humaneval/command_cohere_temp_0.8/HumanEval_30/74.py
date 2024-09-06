```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers found in `l`. The function performs this filtering by using a list comprehension and checking if each element `x` in the list is greater than zero (`x > 0`). 

Here is an example of how to use this function:
```python
result = get_positive([-1, 2, -4, 5, 6])
print(result)
```

Which would print:
```
[2, 5, 6]
```

This demonstrates that the function `get_positive` correctly returns only the positive numbers from the given list, as specified in the problem statement.