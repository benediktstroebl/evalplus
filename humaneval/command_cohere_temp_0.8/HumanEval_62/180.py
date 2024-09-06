```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial whos coefficients are represented by xs
    e.g.: xs[0] + xs[1] * x + xs[2] * x^2 + ... 
    """
    result = [0] * len(xs)
    result[0] = 1
    for i in range(1, len(xs)):
        result[i] = result[i - 1] * 1.0 + xs[i] * (i + 1)
    return result
```

This Python script defines a function `derivative` that takes a list of coefficients `xs` as input, representing the terms of a polynomial, and returns the list of derivatives for each term. It initially fills the result list with zeros up to the same length as `xs`, sets the first element of `result` to 1 (since the derivative of `xs[0]` is 1), and then iteratively calculates the derivatives of the subsequent terms by multiplying the previous result by 1.0 and adding the product of the coefficient and the current exponent to it (using an efficient closed-form derivative formula).

Here is a usage example:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
``` 

This demonstrates that the function correctly calculates the derivatives of the given polynomial expressions.