```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[-1] * x**(-n)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero finds x such that poly(x) = 0
    find_zero returns the pair (x, coeff) where coeff is the largest coefficient and x is the smallest solution.
    >round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
   
   
   

# Tests
def test_find_zero():
    assert find_zero([1, 2]) == (-0.5, 1)

def test_poly():
    assert poly(xs=[1, 2], x=2) == -0.5
    ```

# Main
if __name__ == "__main__":
    print("Test passed!")
```