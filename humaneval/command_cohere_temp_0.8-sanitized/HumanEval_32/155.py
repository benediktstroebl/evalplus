import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[2] * x^2 + ... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first found zero solution.
    Works only for lists xs with an even number of coefficients
    and assumes the largest non-zero coefficient for correctness.
    """
    # Ensure even number of coefficients and extract largest coefficient
    assert len(xs) % 2 == 0
    largest_coeff = max(xs)
    
    # Divide polynomial with largest coefficient as factor
    tmp = [frac for coeff in xs for frac in [coeff, -coeff] if frac != 0]
    factors = math.gcd(*tmp)
    
    solution = [factor * x for factor in tmp for x in range(1, int(math.sqrt(largest_coeff) + 1)) if poly(tmp, x) % factors == 0]
    
    # Solution should be unique
    if len(solution) == 1:
        return solution[0]
    else:
        # If more than one solution, return smallest
        return min(solution)