def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs. """
    n = len(xs) - 1
    deriv = [0] * n
    x = 1
    for i in range(n):
        deriv[i] = xs[i+1] * x
        x *= 1j if i < n-1 else 1    # Handle negative b and c
        x *= i + 1                  # Handle a
    return deriv