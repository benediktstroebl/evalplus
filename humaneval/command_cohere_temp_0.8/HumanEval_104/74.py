```python
def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

This function iterates over each integer `int` in the input list `xs`, checking if `int` contains any even digits when converted to a string. Using the `any()` function with a generating expression inside allows us to efficiently check if any digit of the string representation of the integer is even. The function filters out all integers with even digits and returns the sorted list of remaining elements.

Here is a simple test case to validate the functionality of the function:
```python
test_cases = [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
]

for ints, expected in test_cases:
    actual = unique_digits(ints)
    assert actual == expected, f"Expected {expected}, but got {actual}"
```
```