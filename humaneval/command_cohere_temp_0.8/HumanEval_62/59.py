```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
    derivative_coef = [0] * n
    for i in range(n):
        derivative_coef[i] = xs[i + 1] * (i + 1)
    return derivative_coef
```

The following test cases are included to ensure correctness:
```python
def test_derivative():
    # Test Case 1
    polynomial = [3, 1, 2, 4, 5]
    expected = [1, 4, 12, 20]
    actual = derivative(polynomial)
    assert actual == expected

    # Test Case 2
    polynomial = [1, 2, 3]
    expected = [2, 6]
    actual = derivative(polynomial)
    assert actual == expected

test_derivative()
```

To validate the correctness of the computed derivatives, we can consider a few additional test cases, such as polynomial coefficients with different numeric values and a varied degree of the polynomial. 

This way, we can thoroughly test the `derivative` function and ensure its accuracy in calculating the derivatives of different polynomials.