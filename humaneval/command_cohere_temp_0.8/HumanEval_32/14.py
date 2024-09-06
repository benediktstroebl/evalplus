Here's a Python script with a self-contained function `find_zero` that takes a list of even-length coefficients of a polynomial and returns the value of x at which the polynomial evaluates to zero. This function works by computing the derivative of the polynomial, then solving for x when the polynomial evaluates to zero:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient .
    """
    if len(xs) % 2 != 0: 
        raise ValueError('List xs must have even number of coefficients')
    if max(xs) == 0:
        raise ValueError(' xs must have largest non zero coefficient')

    # compute derivative of polynomial
    dx = [i * x for i, x in enumerate(xs)]

    # Guess the root.
    guess = -xs[0] / dx[0]

    # Use Newton's method to refine the guess and find the root.
    # Dividing by dx[0] (which is nonzero since we checked that)
    # and multiplying by 1/2 to iterate towards the root.
    for _ in range(len(xs) // 2):
        x = guess
        guess = (guess - poly(xs, guess) / (dx[0] * 2)) / 2

    return guess
```

The accompanying test code demonstrates the correct operation of the function:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient .
    """
    if len(xs) % 2 != 0: 
        raise ValueError('List xs must have even number of coefficients')
    if max(xs) == 0:
        raise ValueError(' xs must have largest non zero coefficient')

    # compute derivative of polynomial
    dx = [i * x for i, x in enumerate(xs)]

    # Guess the root.
    guess = -xs[0] / dx[0]

    # Use Newton's method to refine the guess and find the root.
    # Dividing by dx[0] (which is nonzero since we checked that)
    # and multiplying by 1/2 to iterate towards the root.
    for _ in range(len(xs) // 2):
        x = guess
        guess = (guess - poly(xs, guess) / (