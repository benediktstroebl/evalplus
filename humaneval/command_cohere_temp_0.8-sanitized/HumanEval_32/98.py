import math
def find_zero(xs: list) -> float:
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if list length is even
    if len(xs) % 2 == 0:
        # Find discriminant
        discriminant = xs[-1]**2 * xs[0]
        for i in range(1, len(xs)-1):
            discriminant = discriminant - xs[i]**2 * xs[-2]
        # Find root
        root = (-xs[-1] * math.sqrt(discriminant) - xs[0]) / (xs[0] - xs[-1])
        # Check if root is not negative
        if root >= 0:
            return root
    else:
        raise ValueError("Pass an even number of coefficients")