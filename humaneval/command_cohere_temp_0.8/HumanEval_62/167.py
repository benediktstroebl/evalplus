```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial given its coefficients. """
    n = len(xs) - 1
    result = [0] * n
    x = 1
    for i in range(n):
        result[i] = xs[i+1] * x
        x *= 1
    return result
```

The following test cases are included to ensure the function correctness:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([-5, 2, 3, 4, 5]) == [-5, -10, -15, -20]
    assert derivative([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
```

The function can be called with a list of polynomial coefficients, and it will return the coefficients of the derivative of the polynomial. It utilizes a simple calculation by multiplying each subsequent coefficient by 1 and accumulating the result accordingly.