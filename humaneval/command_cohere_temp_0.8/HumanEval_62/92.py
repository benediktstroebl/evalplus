```python
def derivative(xs: list) -> list:
    result = [0]*len(xs)
    degree = len(xs) - 1
    for i in range(len(xs)):
        result[i] = xs[i+1] * degree
        degree -= 1
    return result
```

The following test cases illustrate how the function can be called to verify its behavior:
```python
def test_derivative():
    assert derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert derivative([1, 2, 3]) == [2, 6]
    assert derivative([-1, 2, 3, 4, 5]) == [-2, 6, 12, 20]
    assert derivative([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]
```

This function uses a basic formula to calculate the derivative of a polynomial expression of form `ax^n + bx^(n-1) + ... + cx + d` where `n` is the degree of the polynomial. The derivative of a term `x^n` is `n` times `x^(n-1)`. The function iterates over the list `xs` and accumulates the result accordingly.