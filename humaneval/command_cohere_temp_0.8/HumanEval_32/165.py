Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for polynomial coefficients such that poly(x) = 0.
    Returns only the first found zero.
    Works only for lists of even numbers of coefficients, and assumes the greatest coefficient is the leading coefficient.
    """
    leading_coefficient = max(coefficients)
    half_order = len(coefficients) // 2
    if not len(coefficients) % 2 or not leading_coefficient:
        raise ValueError("List of coefficients must be of even length and leading coefficient must be greater than 0.") 
    if len(coefficients) == 2:
        return -leading_coefficient / (2 * leading_coefficient - coefficients[1])
    else:
        # solve quadratic equation with form x^2 + ... + leading_coefficient x 0
        root = (-leading_coefficient) / (2 * math.sqrt(leading_coefficient ** 2 + sum([coeff ** 2 for coeff in coefficients[1:-1]])))
        return root
```

This script defines two functions: `poly`, which evaluates the polynomial at a given point; and `find_zero`, which finds the point at which a polynomial evaluates to zero. This latter function only works for polynomial lists that have an even number of coefficients and whose largest coefficient is greater than 0. 

To test these functions, you can use the following tests, which are compatible with the ones you provided: 
```python
import math

def test_poly():
    assert poly([1, 2, 3], 2) == 1 + 4 + 12
    assert poly([1, 2, 3, 4], 5) == 1 + 4 * 5 + 3 * 25 + 4 * 125
    assert poly([1, -2, 3, -4], -7) == -2 + 3 * 7 + (-4) * 7 ** 2
    assert poly([1, 2, 3], 0) == 1
    assert poly([1, 2, 3], 1) == 1 + 2 + 3
    assert poly([1, 2, 3, 4], -2) == 1 - 4 + 6 - 8
    assert poly([1, -2, 3, -4], 2) == -2 + 3 - 4

def test_find_zero():
    assert round(find_zero([1, 2]), 2) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
    assert find_zero([1, -2, 3, -4]) == 0
    assert find_zero([1, 2, 3, 4, 5]) == 0
    assert find_zero([0, 0, 0, 0, 1]) == 1

def test_find_zero_error():
    with pytest.raises(ValueError):
        find_zero([1, 2, 3, 4, 5, 6]) 
    with pytest.raises(ValueError):
        find_zero([1, -2, 3, -4, 5]) 
    with pytest.raises(ValueError):
        find_zero([0, 0, 0, 0, 0])