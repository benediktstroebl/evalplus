import math
def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients == coefficients_list such that poly(x) = 0.
    Returns only one solution x, even if there are more than one.
    Works only for lists with even number of coefficients,
    and having the maximum coefficient non-zero.
    """
    # Your code here, remove comments below to keep solving
    if len(coefficients) % 2 == 1:
        raise ValueError('list of coefficients should have even length')
    max_abs_coeff = max(coefficients, key=abs)
    if max_abs_coeff == 0:
        raise ValueError('max coefficient must be non zero')

    # let's make polynomial have form  sum(i=0..n) (x^i) * a_i
    # where max_abs_coeff == a_n
    # x^n * a_n == polynomial_value at x == 0
    # so coeffs[i] == a_{n-i}
    # x == pow(root, i) == pow(coeffs[i], 1/n)
    n = len(coefficients)
    root = max_abs_coeff ** (1/n)
    return round(root, 2)