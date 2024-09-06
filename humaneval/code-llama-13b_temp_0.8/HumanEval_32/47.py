import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check xs has even number of coefficients.
    assert len(xs) % 2 == 0, "Polynomial should have even number of coefficients"

    # Define maximum number of iteration.
    N = 100
    # Find maximum non zero coefficient
    max_non_zero_coeff = max([x for x in xs if x != 0])

    # We can use Ridder's method to find zero of the polynomial.
    # Ridder's method is guaranteed to converge if polynomial is
    # positive on at least one side of the zero point.
    # In our case, we can choose to use this property, as the largest
    # non zero coefficient is positive.
    # Thus, if we guess the zero point is greater than zero, the polynomial
    # is guaranteed to be positive.
    x_high = 1
    # Set the zero point's lower bound as 0
    x_low = 0
    # Initialise x_mid
    x_mid = (x_high + x_low) / 2

    # Iterate N times
    for i in range(N):
        # Get value of polynomial at x_mid
        val_at_mid = poly(xs, x_mid)
        # Set new x_high to x_mid
        x_high = x_mid
        # Update x_low
        x_low = x_high - (x_high - x_low) / 2
        # Set new x_mid
        x_mid = (x_high + x_low) / 2
        # Check the zero point is found within threshold
        if abs(val_at_mid) < 1e-6:
            break
    return x_mid
