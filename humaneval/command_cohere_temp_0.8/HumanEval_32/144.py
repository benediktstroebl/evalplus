Here's a Python script with a self-contained function that solves the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns the result of summing each coefficient multiplied by the corresponding power of x.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.

    Returns:
        float: The result of evaluating the polynomial at the given point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns the value of x that makes the polynomial equal to zero, if it exists.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
    
    Returns:
        float: The value of x at which the polynomial evaluates to zero.
    """
    # Ensure that the list has an even number of coefficients and ignore zero coefficients
    coefficients = [x for x in coefficients if x and len(coefficients) % 2 == 0]
    
    if not coefficients:
        return None
    
    # Ensure 4 coefficients for a quadratic equation
    if len(coefficients) != 4:
        return find_zero(quadratic_subset(coefficients))
    
    # Calculate the discriminant
    a, b, c = coefficients
    discriminant = (b**2 - 4*a*c)
    
    # Return roots of the equation if they exist
    if discriminant > 0:
        return math.sqrt(discriminant) / (2 * a)
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        return None


def quadratic_subset(coefficients: list) -> list:
    """
    Extracts the quadratic subset of coefficients from a longer list of coefficients.
    Returns a list of 4 coefficients (for a quadratic equation) extracted from the provided list.
    
    Args:
        coefficients (list): A list of floats representing the coefficients of the polynomial.
    
    Returns:
        list: A quadratic subset of coefficients.
    """
    if len(coefficients) < 4:
        return []
    else:
        return [coefficients[i] for i in range(len(coefficients)-3, len(coefficients))]

# Test cases
assert round(poly([1, 2], 1), 2) == 1.0
assert round(poly([1, 2], 2), 2) == 2.0
assert round(poly([-6, 11, -6, 1], 1), 2) == -2.0
assert round(poly([1, -11, 2, -3], 2), 2) == -7.0

assert find_zero([1, 2]) == 1.0
assert find_zero([-6, 11, -6, 1]) == 1.0
assert find_zero([1, -11, 2, -3]) == 1.0
assert find_zero([1, 2, 3, 4, 5]) == find_zero(quadratic_subset([1, 2, 3, 4, 5]))

assert find_zero([1, 2, 3, 4, 5, 6]) is None
assert find_zero([1, 2, 3]) is None
```

This script includes two functions: `poly` and `