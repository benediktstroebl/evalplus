```python
def derivative(xs: list) -> list:
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1]*(degree - i)
    return result
```

The derivative of a polynomial of form `xs[0] + xs[1] * x + xs[2] * x^2 + ...`
can be calculated as `d/dx( xs[0] + xs[1] * x + xs[2] * x^2 + ...) = xs[1] + 2xs[2] * x + 3xs[3] * x^2 + ... `

So the derivative of a polynomial is also a polynomial and the above formula gives the coefficients of the derivative polynomial.

The Python script defines a function `derivative` that takes a list of numbers `xs` representing the coefficients of a polynomial and returns the coefficients of the derivative of that polynomial. The function uses a loop to calculate the derivative coefficients, starting from the last coefficient of the original polynomial and uses the formula to calculate the result.

Here is a simple test suite to verify the correctness of the function:
```python
def test_derivative():
    # Single term polynomial
    assert derivative([3]) == [0]

    # Quadratic polynomial
    assert derivative([1, 2, 3]) == [2, 6]

    # Cubic polynomial
    assert derivation([1, 2, 3, 4]) == [2, 6, 12]

    # Multi-term polynomial
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

test_derivative()
``` 
The tests will evaluate the function with different inputs and assert that the corresponding outputs are correct. GOOD LUCK!!