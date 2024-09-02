

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # ders = [xs[i] * j for i in range(len(xs)) for j in [f(i) for f in (lambda i: i+1, lambda i: i-1)] ]
    ders = [[]] * (len(xs) - 1)
    for i in range(len(xs) - 1):
        ders[i] = [xs[i + x] for x in range(len(xs) - i)]
        if i > 0:
            ders[i].append(ders[i - 1][0])
    return [sum(x) for x in zip(*ders)]
