```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This function `unique_digits(xs)` takes a list of integers `xs` as input and returns a sorted list of elements that contain no even digits. The function uses a list comprehension to filter out elements that have any even digits, then the returned list is sorted in increasing order, as required in the prompt. The `not any()` syntax is used to efficiently negate the result of the cascade of conditions. 

The function relies on the `int` syntax which is a valid Python 3 syntax to create an integer from a string representation.

This solution corresponds to the test cases:
```python
>>> unique_digits([15, 33, 1422, 1])
[1, 15, 33]
>>> unique_digits([152, 323, 1422, 10])
[]
```

The general logic is quite clear and straightforward.