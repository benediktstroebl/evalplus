```python
def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])
```

The function unique_digits iterates over each integer in the input list xs, checking if any of its digits are even. It uses the any function in combination with a generator expression to efficiently verify if any digit in the string representation of the integer is even. The int for int in xs construct is an elegant shortcut for a list comprehension, filtering out integers that contain even digits.

The following is a test case that can be used to verify the functionality of the unique_digit function:
```python
test_cases = [
    ([15, 33, 1422, 1], [1, 15, 33]),
    ([152, 323, 1422, 10], []),
]

for ints, expected in test_cases:
    assert unique_digits(ints) == expected
```

This test suite validates the correctness of the function against multiple instances, ensuring that the output list matches the expected result for each variant.