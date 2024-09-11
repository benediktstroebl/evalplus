### Evaluating Polynomials and Finding Zeroes

Below is a self-contained Python script that includes the `poly` and `find_zero` functions as specified, along with a test function to demonstrate their usage:

```markdown
### Code
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... xs[n] * x^n
    
    Args:
        xs (list): A list of coefficients of the polynomial.
        x (float): The point at which to evaluate the polynomial.
        
    Returns:
        float: The value of the polynomial at the point x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial with coefficients xs.
    
    Args:
        xs (list): A list of coefficients of the polynomial. The list must have an even number of coefficients, 
            and the largest non-zero coefficient must be first.
            
    Returns:
        float: A zero of the polynomial. If there are multiple zeroes, this function returns one of them.
    """
    # Convert list of coefficients to a polynomial
    poly = np.poly1d(xs)
    
    # Find roots of the polynomial
    roots = np.roots(poly)
    
    # Select the root with the largest real part
    zero = roots[np.argmax([r.real for r in roots])].real
    
    return zero

### Testing the Functions
def test_find_zero():
    # Test 1: f(x) = 1 + 2x
    print("Test 1:", round(find_zero([1, 2]), 2))
    
    # Test 2: (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    print("Test 2:", round(find_zero([-6, 11, -6, 1]), 2))

test_find_zero()
```

### Explanation
This script uses the `numpy` library to convert the list of coefficients into a polynomial and then find its roots. The `find_zero` function selects the root with the largest real part as the zero of the polynomial. The `test_find_zero` function demonstrates the usage of the `find_zero` function with two test cases.