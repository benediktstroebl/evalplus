```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    result = [0]*(len(xs)-1)
    result.append(1)
    for i in range(len(xs)-1):
        result[i] = xs[i+1] * (i+1)
    return result
```

This Python script defines a function `derivative` taking a list `xs` as input, representing the coefficients of a polynomial, and returns the derivative of this polynomial. The function utilizes a loop to calculate the derivative based on the chain rule, incrementally building up the result list. The initial values are set to 0 and the final value is adjusted to 1 accordingly. Feel free to test this function with other polynomial coefficients to verify its behavior.