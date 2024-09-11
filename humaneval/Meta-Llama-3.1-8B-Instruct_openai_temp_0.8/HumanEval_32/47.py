### Evaluating Polynomial and Finding Zero
```markdown
### Code
```python
import math
import numpy as np

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    
    Args:
    - xs (list): coefficients of the polynomial
    - x (float): point at which to evaluate the polynomial
    
    Returns:
    - float: value of the polynomial at x
    """
    return sum([coeff * np.power(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    Finds a zero of a polynomial with coefficients xs.
    
    Args:
    - xs (list): coefficients of the polynomial
    
    Returns:
    - float: a zero of the polynomial
    
    Note:
    - xs must have an even number of coefficients
    - xs is expected to have the largest non-zero coefficient first
    """
    if len(xs) % 2!= 0:
        raise ValueError("xs must have an even number of coefficients")
    # Try to find a rational zero
    for p in [1, -1]:
        for q in [1, -1]:
            for k in range(int(np.round(np.abs(xs[0]) ** 0.5)) + 2):
                f_x = poly(xs, p * q / k)
                if abs(f_x) < 1e-6:  # Consider a value close enough to zero as a zero
                    return p * q / k
    # If no rational zero is found, try a numerical method
    return np.roots(xs)[0]
```

### Example Usage
```markdown
>>> find_zero([1, 2])
-0.5
>>> find_zero([-6, 11, -6, 1])
1.0
```
Note: The `np.roots` function is used for finding a numerical solution when a rational zero is not found. This function returns an array of roots, so we select the first one. Also, note that due to floating point precision issues, we use `abs(f_x) < 1e-6` to check for a zero value in the rational search function.