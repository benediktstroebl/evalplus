Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms where each term is corresponding coefficient multiplied by x raised to the power of its index in the list.
    i.e. coefficients[0] * x^0 + coefficients[1] * x^1 + ... + coefficients[n] * x^n

    Args:
        coefficients (list): List of coefficients of the polynomial.
        x (float): Evaluation point.

    Returns:
        float: Evaluated polynomial value.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the polynomial polynomial with coefficients coefficients such that poly(x) = 0.

    Args:
        coefficients (list): List of coefficients of a polynomial.

    Returns:
        float: A solution x such that poly(x) = 0.
    """
    # Check if list has an even number of coefficients and if it does, 
    # then reverse the list so we can use coefficients with index ranging from 0 to n-1
    if len(coefficients) % 2 == 1:
        coefficients.reverse()
    # Ensure list has larger non-zero coefficient at index 0
    if coefficients[0] == 0:
        coefficients.pop(0)
        coefficients.reverse()
        coefficients[0] = 0
    half_degree = len(coefficients) // 2
    return _find_zero(coefficients, half_degree)


def _find_zero(coefficients: list, degree: int) -> float:
    """
    Helper function for find_zero that employs the division method to find a zero. 
    It tries to split the polynomial into two polynomials with degrees lesser than half_degree
    by detecting patterns in the coefficients employing some if statements.
    Then it proceeds to find the zero for the polynomial of degree half_degree
    by successive approximation starting with an initial guess of 
    (-coefficients[half_degree - 1] / (2 * coefficients[half_degree]))

    Args:
        coefficients (list): List of coefficients of a polynomial.
        degree (int): Degree of the polynomial, must be equal to len(coefficients) / 2

    Returns:
        float: A solution x such that poly(x) = 0.
    """

    # Some coefficients may be zero and they should not affect the result, 
    # so we remove them from the list temporarily
    while len(coefficients) < degree + 1:
        if not coefficients:
            return None
        if coefficients[-1] == 0:
            coefficients.pop()
        else:
            break

    # If the leading coefficient is not 1, then employ x +- sqrt(leading_coefficient)/leading_coefficient
    if coefficients[0] != 1:
        x = _find_zero_helper(coefficients, degree, 2)
    # If the leading coefficient is 1, then employ x +- sqrt(leading_coefficient)/2
    else:
        x = _find_zero_helper(coefficients, degree, 1)

    return x


def _find_zero_helper(coefficients: list, degree: int, coefficient_multiply: int) -> float:
    """
    Helper function for _find_zero that employs the division method to find a zero. 
    It uses a starting guess of (-coefficients[degree - 1] / (2 * coefficients[degree