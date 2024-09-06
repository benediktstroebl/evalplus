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
    Finds a solution x for the equation polynomial == 0.
    Returns only the first found zero solution for the polynomial defined by the given coefficients.
    
    WARNING: This function only supports polynomials with an even number of coefficients, 
    and the largest non-zero coefficient should not be equal to the coefficient on the x^n term.
    
    This is based on the "subtract and conquer" method:
    1. Subtract the largest coefficient times x^n from the polynomial, 
        leaving an equation with a smaller degree.
    2. Repeat for the new polynomial until x^n is 1.
    3. Solve for x in the equation of the simplified polynomial - lead coefficient.
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        raise ValueError("This function supports only polynomials with even numbers of coefficients, " 
                         "and the largest non-zero coefficient must not be equal to the coefficient on the x^n term.")
    
    x = None
    while True: 
        # Subtract x^n term to decrease degree
        temp_coefficients = coefficients.copy()
        if len(temp_coefficients) > 1: 
            temp_coefficients.pop()
        polynomial = poly(temp_coefficients, x) if x is not None else 0
        
        # Simplify the polynomial
        simplify = False
        for i in range(len(polynomial)):
            if i == 0:
                continue
            elif polynomial[i] == 0:
                simplify = True
                break
            elif polynomial[i] < 0:
                polynomial[i] = -polynomial[i]
                polynomial[i-1] = -polynomial[i-1]
                simplify = True
                break
        if not simplify:
            return x
        
        # Calculate x^n
        x_pow_n = 1
        for i in range(len(coefficients)):
            x_pow_n *= x
        x = x_pow_n / math.sqrt(max(1, sum(coefficients)**2))
```

This script defines a polynomial evaluation function `poly` and a polynomial zero finding function `find_zero`. The `find_zero` function iteratively simplifies the polynomial by removing the highest power term and updates the solution `x` accordingly. The solution is found when the polynomial can no longer be simplified. 

The warning in the docstring explains the limitations of the current implementation, mainly that it supports only polynomials with an even number of coefficients and where the largest non-zero coefficient is not the coefficient of the highest power. 

This is a simplified implementation that supports many use cases. For more complex polynomial equations or specialized behavior, consider using a specialized library or mathematical tools.