```python
def derivative(xs: list) -> list:
    result = [0] * (len(xs) + 1)
    result[0] = 1
    for i in range(1, len(xs)):
        result[i] = result[i - 1] * len(xs) + xs[i - 1] * (len(xs) - 1)
    return result
```

The derivative of a polynomial is given by:
```
(x^n) = n * (x^(n-1)) + n*(n-1) * x^(n-2) + ... + 1 * x + 0
```

Where the coefficient of the derivative is given by:
```
(n * (x^(n-1)) + n*(n-1) * x^(n-2) + ... + 1 * x + 0)
```

Thus, the following terms in the derived polynomial are given by:
```
Result[i] = i * (len(xs) * xs[i-1] + (len(xs) - 1) * xs[i])
```

The base case of the recursion is when i = 0, in which case:
```
Result[0] = 0
```

This generates the complete derived polynomial.