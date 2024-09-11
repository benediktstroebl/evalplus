### Polynomial Evaluation and Zero Finding

Below is a Python script that defines two functions: `poly` to evaluate a polynomial and `find_zero` to find a zero of a polynomial.

```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    Finds a zero of a polynomial with coefficients xs.
    
    This function assumes that xs is a list with an even number of coefficients
    and that the largest non-zero coefficient is at an even index.
    
    It uses the fact that if x is a root of the polynomial, then x^2 is a root
    of the polynomial with coefficients xs[0] + xs[2], xs[1] + xs[3],...
    
    This means that we can repeatedly square the current estimate until it is close
    enough to zero.
    
    :param xs: List of coefficients of the polynomial
    :return: An approximate zero of the polynomial
    """
    # handle case of linear function
    if len(xs) == 2:
        return -xs[1] / xs[0]

    # initialize estimate
    x = 10.0  # any large number will do
    
    # repeat until estimate is close enough to zero
    while abs(x) > 1e-6:
        # calculate new estimate by squaring current one
        x = -poly(xs[0::2], x) / poly(xs[1::2], x)
    
    return x


# test cases
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
    print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Note that the `find_zero` function assumes that the input polynomial has a real root and that the largest non-zero coefficient is at an even index. This function uses a simple iterative method to find the root: it starts with an initial estimate and repeatedly squares it until the estimate is close enough to zero.