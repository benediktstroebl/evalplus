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
    if len(xs) % 2 != 0:
        raise ValueError("Polynomial must have even number of coefficients.")
    if len(xs) == 2:
        # f(x) = x + 1
        return -xs[0] / xs[1]
    # Slope = 1 / (m*x^2 - b)

    def find_zeros(xs: list, a: int, b: int):
        """
        >>> find_zeros([1, 2, 3, 0, -6, 11, -6, 1], 1, 1)
        [(-3 + 4.0*sqrt(6))/(2*sqrt(2))]
        """
        if len(xs) == 2:
            return [-xs[0] / xs[1]]
        subtract = [xs[0] * i - xs[1] * i ** 2 for i in range(2, len(xs))]
        # print(subtract)
        # Can't use list.index() here due to potential duplicate
        first_negative = [n for n in range(len(subtract)) if subtract[n] < 0]
        if len(first_negative) == 0:
            # No negative coefficient.
            return [-a / (2 * b)]
        elif len(first_negative) == 1:
            # Only one negative coefficient.
            return [(a - xs[0]) / (2 * xs[1])]
        else:
            # Multiple negative coefficients.
            # Need to figure out the real roots of following polynomial
            # p(x) = a + b*x + c*x^2 + ... + d*x^n
            # here d is the first non-negative coefficient from previous list.
            # Suppose f(x) is a real number, then
            # m*x^2 - (b + d)*x + c = 0
            # => (-b + d)*x^2 - 2d*x - c = 0
            # => (b + d)*x + c = -d
            # => x = -d / b + sqrt(b^2 - 4ac) / 2a
            d = first_negative[0