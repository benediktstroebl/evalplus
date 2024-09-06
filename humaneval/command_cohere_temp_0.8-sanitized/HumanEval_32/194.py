import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation polynomial = 0.
    Only returns the first solution, even if there are multiple zeros.
    Moreover, the function only accepts lists of coefficients of length an even number,
    since odd degree polynomials cannot have zeros.
    Furthermore, the function only accepts lists of coefficients with the largest non-zero coefficient,
    since the latter guarantees the uniqueness of a zero.
    """
    if len(coefficients) % 2 == 0:
        # even number of coefficients
        # largest coefficient
        largest_coeff = max(coefficients)

        if largest_coeff != 0:
            # construct polynomial f(x) = sum(xi * x^(2i) )
            # such that f(x) = 0 at the zero and
            # let g(x) be the polynomial of lower degree
            # such that g(x) = f(x) at the zero
            x0 = poly(coefficients, 0)
            x1 = poly(coefficients, x0)
            x2 = poly(coefficients, x1)
            xn = x2
            for _ in range(len(coefficients) // 2):
                xn = poly(coefficients, xn)
            return xn
        else:
            raise ValueError("No point of zero for given polynomial!")
    else:
        raise ValueError("List of coefficients must have an even length!")