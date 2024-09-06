import math
def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x**i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients such that poly(x) = 0.
    Returns only the first found zero solution, even if there are more.
    Works only for lists coefficients having even number of coefficients
    and largest non-zero coefficient, as it guarantees a solution.
    """
    # Your code here.
    # You may want to implement bisection method
    # https://en.wikipedia.org/wiki/Bisection_method
    import numpy as np
    n = len(coefficients) // 2
    x0 = np.maximum(coefficients[n]/coefficients[n-1], 1e-6)
    x1 = 10
    while True:
        x = (x0 + x1) / 2
        if poly(coefficients, x) == 0:
            return x
        else:
            if abs(x1 - x0) < 1e-6:
                break
            elif poly(coefficients, x) > 0:
                x0 = x
            else:
                x1 = x