def simplify(x, n):
    """
    Simplify the expression x * n.
    Returns True if x * n evaluates to a whole number, and False otherwise.
    x and n are string representations of fractions in the format <numerator>/<denominator>.
    Both numerator and denominator are expected to be positive whole numbers, and denominators are not allowed to be zero.
    """
    x, n = Fraction(x), Fraction(n)
    return x * n == int(x * n)