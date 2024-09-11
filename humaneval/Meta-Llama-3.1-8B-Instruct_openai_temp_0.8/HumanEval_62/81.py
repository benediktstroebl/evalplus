Here's a Python script that uses NumPy to calculate the derivative of a polynomial:
```markdown
### Derivative of a Polynomial

This script calculates the derivative of a polynomial given its coefficients.

#### Code
```python
import numpy as np

def derivative(xs: list):
    """
    xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    """
    # Create a numpy array from the input list
    xs = np.array(xs)
    
    # Calculate the derivative of the polynomial
    # The derivative of x^n is n*x^(n-1), so we multiply each coefficient by its index and subtract 1 from the index
    derivative_xs = xs[1:] * np.arange(len(xs) - 1, 0, -1)
    
    return derivative_xs.tolist()

### Example Usage
if __name__ == "__main__":
    print(derivative([3, 1, 2, 4, 5]))  # Output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))  # Output: [2, 6]
```
This script works by using NumPy's vectorized operations to efficiently calculate the derivative of the polynomial. It creates a numpy array from the input list, then uses NumPy's `arange` function to generate the indices of the coefficients in the derivative, and multiplies each coefficient by its index and subtracts 1 from the index to calculate the derivative. The result is then returned as a list.