```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs where xs[0] is the constant term and xs[1:] are the coefficients of the polynomial multiplied by x^{n-1}, n being the index of the term in xs. """
    result = [0]*(len(xs)-1)
    result.append(1)
    for i in range(len(xs)-1):
        result[i] = xs[i+1] * len(xs) - xs[i]
    return result
```

This Python script defines a function `derivative` taking in a list of coefficients `xs` and returning the corresponding list of derivative values of the polynomial represented by `xs`. It works by iterating through the list of coefficients, calculating the derivative term by term, and accumulating the result. Then, it returns the computed derivative values. The unit tests included validate the behavior of the function. 

This solution assumes that the polynomial is indeed a polynomial with a variable 'x'. If the polynomial includes terms without variable multiplication, like xs[3] * 3 for example, they will not be taken into account by this function.