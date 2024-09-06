```python
def derivative(xs: list) -> list:
    """
    Compute the derivative of a polynomial expressed as a list of coefficients.

    Args:
        xs (list): Coefficients of the polynomial, in order of increasing power of x.

    Returns:
        list: Derivative of the polynomial, represented as a list of coefficients.

    Example:
        >>> derivative([3, 1, 2, 4, 5])
        [1, 4, 12, 20]
    """
    derivative_sum = [0] * (len(xs) + 1)
    for i in range(len(xs)):
        for j in range(i + 1, len(xs) + 1):
            derivative_sum[j] += xs[i] * j
    return derivative_sum[:-1]
```

This approach uses a dynamic programming approach, storing intermediate results in the `derivative_sum` list to efficiently compute the derivative. 

You can test the function by calling it with a list of polynomial coefficients as an argument. 
For example:
```python
test_cases = [
    ([3, 1, 2, 4, 5], [1, 4, 12, 20]),
    ([1, 2, 3], [2, 6]),
    ([5, 5, 5, 5], [10, 10, 10, 10]),
]

for expected, input_ in test_cases:
    assert derivative(input_) == expected
```

This block of code tests the function with different test cases to ensure it matches the expected output.