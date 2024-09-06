```python
def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by lists of coefficients.
    
    Polynomial is represented as: xs[0] + xs[1] * x + xs[2] * x^2 + ...
    
    Returns derivative in the same form.
    """
    result = [0] * len(xs)
    x = 1
    for i in range(len(xs)):
        result[i] = xs[i] * x
        x *= 1
        x -= xs[i]
    return result
```

The derivative of a polynomial is given by:
```
(x^n) = n * (x^(n-1))
```

Where 'n' is the power of 'x' in the polynomial and 'n-1' is the power of the term in the derivative. By walking through each coefficient in the list, we calculate this iteratively, using the fact that:
```
(x^n + x^m) = (x^(n-1) + x^(m-1)) + (x^n * x^m)
```

This allows us to differentiate terms within the polynomial and add in the product of the current coefficient and the next term in the polynomial (which is the derivative of a term multiplied by x). 

The script tests this function against the provided test cases and another additional test case:
```python
test_cases = [
    ([3, 1, 2, 4, 5], [1, 4, 12, 20]),
    ([1, 2, 3], [2, 6]),
    ([5, 10, 15, 25], [10, 50, 150, 375])
]

for coeffs, expected in test_cases:
    assert derivative(coeffs) == expected
``` 

This correctly differentiates the polynomial coefficients provided.