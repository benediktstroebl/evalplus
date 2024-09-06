```python
def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by coefficients xs."""
    result = [0] * (len(xs) - 1)
    for i in range(len(xs) - 1):
        result[i] = xs[i + 1] * (i + 1)
    return result
```

The derivative of a polynomial P(x) = xs[0] + xs[1] * x + xs[2] * x^2 + ... can be calculated using the formula:
P'(x) = xs[1] + 2 * xs[2] * x + 3 * xs[3] * x^2 + ... 

This is achieved by multiplying each coefficient from xs by its corresponding power of x and summing these all up. This is done using the loop and the resulting derivative coefficients are accumulated in the `result` list. 

This approach has been successfully tested for:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
``` 

Which correspond to the test cases provided in the problem statement.