def derivative(xs: list) -> list:
    """Return the derivative of a polynomial represented by lists of coefficients.

    Polynomial is represented in the form:
        xs[0] + xs[1] * x + xs[2] * x^2 + ...

    Returns a new list with the derivative of the polynomial, in the same form.

    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    ans = [0] * (len(xs) + 1)
    for i in range(1, len(xs)+1):
        ans[i] = xs[i-1] + i * ans[i-1]
    return ans[:-1]