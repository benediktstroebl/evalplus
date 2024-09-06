```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x that makes poly(x) = 0.
    find_zero returns only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.

    # Test
    generate a polynomial of degree 4
    polynomial = [1, 2, 3, 4]
    x = 4.0
    result = poly(list(polynomial), x)
    assert result == 20.0
    print("Result is:", result)

    # Test 2.0
    polynomial of degree 2 with x = -2.0
    result = poly(list([2.0]), x)
    print("Result is:", result)

    # Test 3.0
    polynomial of degree 3 with x = -3.0
    result = poly(list([(-3.0, -2.0, -3.0]), x)
    test result

    # Test 4.0
    polynomial of degree 3 with x = -4.0
    result = poly(list([(-4.0, -3.0, -3.0]) * x)
    print("Result is:", result)

    # Test 5.0
    polynomial of degree 4 with x = 1.0
    result = poly(list([1.0, 2.0, 3.0, 4.0])
    print("Result is:", result)
```