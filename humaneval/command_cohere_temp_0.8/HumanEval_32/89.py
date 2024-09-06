Here's a Python script that includes a function to solve the problem:
```python
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
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are more.
    Works only for lists with even number of coefficients,
    and skips lists with smallest coefficient == 0.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return None

    # We make sure that the polynomial has a positive leading coefficient,
    # that is, we take abs(|a|) of the smallest coefficient (a), and flip the sign.
    # Then we multiply the rest of the coefficients by |a|
    #Notable: multicpling by -1 is equivalent to changing the sign of the polynomial
    smallest_coefficient = min(coefficients)
    assert smallest_coefficient != 0
    flip = 1 if smallest_coefficient > 0 else -1
    coefficients = [abs(coefficient) * flip for coefficient in coefficients]
    
    #We flip the sign of the polynomial
    x = None
    prev_sign = 1
    while x == None:
        sign = -1 if prev_sign == 1 else 1
        interval_start = max(coefficients) / (sign * 2)
        interval_end = (min(coefficients) / (sign * 2))
        x_approx = (interval_end + interval_start) / 2
        x = poly(coefficients, x_approx)
        if x == 0:
            # If we found a solution, and it is not x_approx, it means
            # that the polynomial changes the sign on this interval
            # We have to find the exact position of this sign change
            # by bisection method
            x_prev = x_approx - 1 if prev_sign == 1 else x_approx + 1
            while x_prev != x:
                x_mid = (x_prev + x_approx) / 2
                if poly(coefficients, x_mid) == 0:
                    x_approx = x_mid
                else:
                    x_prev = x_mid
            # Here we found the exact position of the sign change,
            # and because of the way we constructed the polynomial,
            # the solution is on the right side of this position
            x = x_approx
        prev_sign = -prev_sign
    return x
```

The provided code includes two functions, `poly` and `find_zero`. The `poly` function takes a list of coefficients and a value `x` as input and returns the value of the polynomial at the given point `x`. The `find_zero` function takes a list of coefficients as input and returns the value of the first zero of the polynomial, that is the first value of `x` for which `poly(x)` equals `0`. This function works for lists with an even number of coefficients and skips lists with the smallest coefficient equal to zero.

The `find_zero` function exploits the fact that if we have a polynomial of an even order with the largest coefficient not equal to zero, then such a polynomial has at least one zero point. Moreover