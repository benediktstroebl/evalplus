```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by xs. """
    n = len(xs) - 1
   derivative_coefficients = [0] * n
    for i in range(n):
        derivative_coefficients[i] = xs[i+1] * (i + 1)
    return derivative_coefficients
```

The following test cases are provided to ensure correctness of the function:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([-5, 2, 3, 4, 5]) == [-5, 14, 24]
    assert derivative([0, 0, 0, 0, 5]) == [0, 0, 0, 0, 10]
```

The function `derivative` takes a list `xs` as input, which represents the coefficients of a polynomial in standard form: `xs[0] + xs[1] * x + xs[2] * x^2 + ...`. The function calculates the derivative of this polynomial and returns the coefficients of the derivative in the same form. 

To compute the n-th derivative coefficient, the function uses the formula `d(x^n) / dx = n * x^(n-1)`. It then iterates through the input coefficients, appropriately calculating each derivative coefficient by multiplying it with the corresponding power of x and the current coefficient. Finally, the function returns the computed derivative coefficients.