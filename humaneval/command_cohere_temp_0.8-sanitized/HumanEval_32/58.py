import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial with coefficients coefficients such that poly(x) = 0.
    Returns only the first found zero solution, if multiple zeros exist.
    
    Solution is found using the following steps:
        1. Calculates corresponding polynomial p(x) using the poly() function
        2. Finds x such that p(x) = 0
        3. Returns x
    """
    n = len(coefficients)
    # Check for an error case
    if n % 2 == 1 or coefficients[n // 2] == 0:
        raise ValueError("List coefficients must have an even number of elements and include a largest non-zero coefficient to guarantee a solution.")

    # Assurance that the non-zero coefficient is positive
    if coefficients[n // 2] < 0:
        coefficients[n // 2] = -coefficients[n // 2]
        x = -1 * find_zero(coefficients)
        return -x

    # calculates polynomial p(x) using poly() function
    p = poly(coefficients, x)

    # Finds x0 in interval x0 <= x <= 1.0 such that p(x0) = 0
    x0 = find_zero_in_range(p, x, 1)

    return x0
def find_zero_in_range(p, x, to):
    """
    Finds x in interval [x_lower_bound, 1.0] such that p(x) = 0.
    If no such point exists within the interval, returns x_lower_bound
    """
    while p > 0:
        if x == to:
            return x
        x += 1
        p -= x
    return x