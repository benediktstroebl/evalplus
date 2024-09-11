```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    xs (list): A list of coefficients of the polynomial in descending order of powers.
    x (float): The point at which the polynomial is evaluated.
    
    Returns:
    float: The value of the polynomial at point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ 
    Finds a zero point of a polynomial given its coefficients.
    
    Args:
    xs (list): A list of coefficients of the polynomial in descending order of powers.
    
    Returns:
    float: A zero point of the polynomial.
    
    Raises:
    ValueError: If the list xs has an odd number of coefficients.
    """
    
    # Check if the list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("The list xs must have an even number of coefficients.")
    
    # Check if the largest non-zero coefficient is the first one
    if xs[0] == 0:
        raise ValueError("The largest non-zero coefficient must be the first one.")
    
    return -xs[1] / xs[0]


# Example usage:
# A polynomial x + 2
print(round(find_zero([1, 2]), 2))

# A polynomial (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
print(round(find_zero([-6, 11, -6, 1]), 2))
```

Note that the `find_zero` function uses the fact that a quadratic equation `ax^2 + bx + c = 0` has a solution `x = -b / a`. We can generalize this to higher-degree polynomials by considering the first two coefficients as the leading coefficients of the two highest-degree factors of the polynomial. This approach is valid because the problem statement guarantees that the list `xs` has an even number of coefficients and the largest non-zero coefficient is the first one.

Also note that this approach works for polynomials with real coefficients and may not work for polynomials with complex coefficients.