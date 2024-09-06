import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns xs[0] + xs[1] * x + xs[1] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for the polynomial xs such that poly(x) = 0.
    Only returns the first solution found.
    Only accepts lists xs with an even number of coefficients,
    and with the largest non-zero coefficient capitalized.
    """
    if len(xs) % 2 == 1:
        raise ValueError('List xs must have an even number of coefficients.')
    xs = [float(x) for x in xs]
    biggest_coeff = max(xs)
    if biggest_coeff == 0:
        raise ValueError('List xs must have a non-zero largest coefficient.')
    
    xs.sort()
    x = 0
    tangent_guess = xs[0] / 2
    print('Using x =', tangent_guess, 'as an initial guess.')
    
    while abs(poly(xs, x)) > 1e-6:
        x_plus = x + tangent_guess
        x_minus = x - tangent_guess
        if abs(poly(xs, x_plus)) < 1e-6 and abs(poly(xs, x_minus)) < 1e-6:
            return x_plus
        x = x_plus if abs(poly(xs, x_plus)) < abs(poly(xs, x_minus)) else x_minus
        tangent_guess *= 2
    return x