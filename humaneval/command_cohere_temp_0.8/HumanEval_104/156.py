```python
def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This function `unique_digits(xs)` takes a list of integers `xs` as input and returns a sorted list of elements that contain no even digits. The function uses a list comprehension to iterate through each element in `xs`, checking if an integer is suitable to be included in the final result by using the `any()` function with a generator expression. This generator expression, `(int % 2 == 0 for digit in str(int))`, simulates looping through each digit in the string representation of the corresponding integer (`str(int)`), and checking if it is even (`int % 2 == 0`). The `not any()` condition effectively checks if no digit is even, fulfilling the requirement of the algorithm.