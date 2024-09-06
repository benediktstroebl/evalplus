```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs.sum([coeff * * x**_power(i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x and evaluates polynomial at that point
    """
    return next((x, y) for x, y in zip(find_zero_list(xs), xs) if y == 0)

def find_zero_list(xs: list):
    """
    xs are coefficients of a polynomial
    return [x for x in xs if x != 0]

def test_find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    test_find_zero test if find_zero returns a single value for the given polynomial
    """
    return all(y == 0 for y in find_zero(xs))

# Example usage
xs = [1, 2]
x = 3.0
print(poly(xs, x))
print(find_zero(xs))
```
This script defines a function `poly` that computes the polynomial expression for a given list of coefficients `xs` at a given `x` value. The `find_zero` function finds the zeros of this polynomial expression. The `find_zero_list` function returns a list of non-zero elements from the input list. The `test_find_zero` function tests if `find_zero` returns a single value for the given polynomial.  Finally, the example usage demonstrates the script's functionality by evaluating the polynomial at a specific `x` value and then checking if the function `find_zero` returns a single value.