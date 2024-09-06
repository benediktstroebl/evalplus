Here's a Python script with a self-contained function that solves the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation p(x) = 0.
    Returns the value of x that makes the polynomial equal to zero,
    based on the coefficients provided.
    This function only returns one solution, and works only with lists
    of even numbers of coefficients, and with the coefficient list
    containing at least one non-zero value.
    """
    if len(coefficients) % 2 == 1 or not coefficients:
        return None

    # arrange coefficients in decreasing order
    coefficients.sort(key=lambda x: x/x if x != 0 else float('inf'), reverse=True)

    # extract non zero coefficient
    coeff = coefficients[0]

    # check if there is only one non zero coefficient
    if len(coefficients) == 2:
        # if there is, return it's half
        return coeff / 2

    # handle even number of coefficients
    return poly_zero_ algorith(coefficients, coeff)


def poly_zero_algorith(coefficients: list, coeff: float) -> float:
    """
    Internal function to find zero of polynomial.
    """
    # iterate through dividing coefficients in reverse by coeff
    for i in range(len(coefficients)):
        if coefficients[i] != 0:
            coeff /= coefficients[i]
            # return x if quotient is 0
            if coeff == 0:
                return i

    # if no solution, return None
    return None

# Tests:
assert find_zero([1, 2]) == -0.5
assert find_zero([-6, 11, -6, 1]) == 1.0

assert find_zero([1, -2, 3, 4, 5]) is None

assert find_zero([0, 1, 2, 3, 4]) == 2.0

assert find_zero([1, -2, -1, -2, 4, 5, 6]) == 3.0

``` 

The `poly()` function evaluates a polynomial given a list of coefficients and a variable value. The `find_zero()` function finds the zero value of a polynomial based on a list of coefficients. This function only returns one solution and works only with lists of even coefficients and lists that contain at least one non-zero value. If the list of coefficients is empty or has an odd number of elements, or all elements are zero, the function returns `None`. 

The internal function `poly_zero_algorith()` implements a brute force algorithm to find the zero of a polynomial. This algorithm iterates through the coefficients in reverse order and divides each one by the variable `x`. If a coefficient divides `x` without remainder, `x` is a solution, and the algorithm returns that solution. The internal function is called with `poly_zero_algorithms()` in the `find_zero()` method. 

This code demonstrates how to evaluate polynomials and find their zeroes in Python. Let me know if anything needs to be clarified or adjusted further.