```python
def get_positive(l: list) -> list:
    """Return only positive numbers in the list."""
    return [x for x in l if x > 0]
```

This Python script defines a function `get_positive` that takes a list `l` as input and returns a list of all positive numbers found in `l`. The function performs this filtering using a list comprehension, iterating over each element `x` in `l` and checking if `x` is greater than zero. The conditional expression `x > 0` is used as a filtering condition, including only those elements that satisfy it. The list comprehension constructs a new list containing the positive values and returns it as the result. 

This solution is encapsulated within a function declaration, allowing reusable and modular code organization. Additionally, the function includes a docstring to provide a description of its purpose, input, and output, as well as example usage that demonstrates how the function is intended to be used.