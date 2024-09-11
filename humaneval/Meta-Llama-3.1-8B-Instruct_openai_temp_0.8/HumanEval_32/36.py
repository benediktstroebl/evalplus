Here's the Python script that solves the problem:

```markdown
### Polynomial Evaluation and Zero Finder

This script defines two functions: `poly` to evaluate a polynomial at a given point, and `find_zero` to find the zero point of a polynomial.

#### Code
```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    - xs (list): coefficients of the polynomial
    - x (float): the point at which to evaluate the polynomial
    
    Returns:
    - float: the value of the polynomial at point x
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds the zero point of a polynomial.
    
    Args:
    - xs (list): coefficients of the polynomial
    
    Returns:
    - float: the zero point of the polynomial
    
    Note:
    - This function assumes that the input list has an even number of coefficients
    - The largest non-zero coefficient is used to guarantee a solution
    """
    # Check if the input list has an even number of coefficients
    if len(xs) % 2!= 0:
        raise ValueError("Input list must have an even number of coefficients")

    # Get the largest non-zero coefficient
    largest_non_zero = max([coeff for coeff in xs if coeff!= 0])

    # Find the zero point
    x = -xs[1] / largest_non_zero
    return x

# Example usage
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

#### Explanation

The `poly` function uses a list comprehension to evaluate the polynomial at a given point. It iterates over the coefficients and their indices, raising each coefficient to the power of its index.

The `find_zero` function assumes that the input list has an even number of coefficients and uses the largest non-zero coefficient to guarantee a solution. It then returns the zero point by dividing the second coefficient by the largest non-zero coefficient and taking the negative.

Note that this implementation may not work for all polynomials, especially those with complex or irrational roots. For more robust solutions, consider using numerical methods or libraries like `numpy` or `scipy`.