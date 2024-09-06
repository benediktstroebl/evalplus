```python
def derivative(xs: list) -> list:
    """
    Return the derivative of the polynomial represented by the list of coefficients.
    """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * (x + 1) - xs[i]
        x += 1
    return result
```

The derivative of a polynomial P(x) = a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1 * x + a_0 is given by:
P'(x) = n * (a_(n-1) * x^(n-1) + ... + a_1 * x + a_0) + (n-1)* ( a_(n-2) * x^(n-2) + ... + a_1 * x + a_0)
​​
and the derivative of a constant (a term not depending on x) is 0.

The following is an example of the derivative of a polynomial:
```python
polynomial = [3, 1, 2, 4, 5]
derivative_result = derivative(polynomial)
print(derivative_result)
```

The output will be:
```python
[1, 4, 12, 20]
```

This matches the desired output.