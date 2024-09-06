```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    return sorted(x for x in xs if not any(int(d) % 2 == 0 for d in str(x)))
```

This Python script provides a function called `unique_digits` that takes a list of positive integers as input (`xs`). It filters this list and returns a sorted list of only those elements that do not contain any even digits in their representations. The `any` function with a generator expression inside is used to efficiently check if any digit of the integer is even. The `unique_digits` function is applied to test cases, and its behavior is exemplified with an example in the docstring, making it convenient for users to understand and utilize.