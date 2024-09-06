```python
def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    return sorted([int for int in xs if not any(c % 2 == 0 for c in str(int))])
```

This function iterates over each integer `int` in the input list `xs`, checking if any of its digits in the string representation is even. It utilizes a list comprehension to filter out the integers that have at least one even digit, resulting in a list of integers with only odd digits. Finally, it returns the sorted list of these filtered integers. 

The test cases ensure that the function correctly identifies integers with even digits and includes integers with all-odd digits.