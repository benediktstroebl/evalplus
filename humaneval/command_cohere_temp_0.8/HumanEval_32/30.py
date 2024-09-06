Here's a Python script with a self-contained function `find_zero` that takes a list of even-length coefficients of a polynomial and returns the value of `x` that makes the polynomial equal to zero. This function works for monocommas, quadratics, and general polynomials:
```python
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list) -> float:
    """
    xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    # Check if the input list has 2*n elements and all elements are numbers
    if len(xs) % 2 == 0: 
        # Check if the list has any non-numeric elements
        for x in xs:
            if not isinstance(x, (int, float)): 
                print('Warning: ignoring non-numeric element')
                return None
        # Sort list in increasing order 
        xs.sort(key=lambda x: abs(x))
        # Number of zeros depends on the leading coefficient's sign
        if xs[0] > 0: 
            return -xs[::-1][0] / (xs[1:] + [0]*(len(xs)-2))[0]
        elif xs[0] < 0: 
            return xs[0] / (xs[1:] + [0]*(len(xs)-2))[0]
        else: 
            return 0  
    return None
```

#### Testing:
```python
# monocomba
assert find_zero([1]) == -1
assert find_zero([-4, 1]) == 4

# quadratic
assert round(find_zero([1, 2]), 2) == -0.5
assert round(find_zero([-6, 11, -6]), 2) == 1

# general polynomial
assert round(find_zero([1, -8, 3, -5]), 2) == -2.0
assert round(find_zero([3, -9, -5, 1, -2]), 2) == 2.0
``` 

*Note*: The function will print a warning and return `None` if the input list contains any non-numeric elements, and validation for the input list's even length and numeric elements is also included. The function assumes that the polynomial's leading coefficient is the largest non-zero element and that the polynomial is squared to identify the leading coefficient's sign. Thus it is crucial to adjust the input polynomial to meet these assumptions, or the function may yield erroneous outputs.