import math
def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms xs[0] + xs[1] * x + xs[1] * x^2 + .. xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs):
    """
    Finds a solution x for polynomial xs such that poly(x) = 0.
    Returns only the first solution x, even if there are multiple zeros.
    Works only for lists xs with an even number of coefficients,
    and assumes the largest non-zero coefficient for uniqueness.
    """
    # Ensure even number of coefficients and extract largest coeff
    assert len(xs) % 2 == 0
    max_coeff = max(xs)
    
    # Sort xs in descending order
    xs.sort(reverse=True)
    
    # Initialize lst vector and iteratively update
    lst = [0] * (len(xs) // 2)
    for i in range(len(xs) // 2):
        while lst[-1] <= xs[i] and len(lst) > 1:
            lst.pop()
        lst.append(xs[i])
    
    # Initialize guess and update while moving towards origin
    x = 1e10
    while len(lst) > 1:
        x_mid = (x + lst[0] / lst[1]) / 2
        if abs(poly(xs, x_mid)) < 1e-6:
            x = x_mid - max_coeff / x_mid
            break
        elif poly(xs, x_mid) > 0:
            x = x_mid
        else:
            lst.pop(0)
    
    return x