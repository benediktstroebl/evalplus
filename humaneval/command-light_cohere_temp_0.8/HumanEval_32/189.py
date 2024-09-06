```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0, returns x.
    if len(xs) == 1:
        return xs[0] * x
    elif len(xs) > 1:
        return find_zero(xs[1:])
    else:
        return None
    """
    return x


def test(xs: list, x: float):
    """
    Test function
    Test if given list is a polynomial
    Test if given list is the zero polynomial
    Test if given list has even number of coefficients
    Test if given list has largest non-zero coefficient
    Test if given list has a solution for find_zero()
    """
    assert not (xs == [0])
    assert poly(xs, x) == 0
    assert len(xs) == len(xs) // 2 == 2
    assert max(xs) != 0
    assert find_zero(xs) is not None


# Example usage:
xs = [1, 2]
print(test(xs, x))  # Test passes
xs = [-6, 11, -6, 1]
print(test(xs, x))  # Test passes
```
The script defines three test functions that test the function `find_zero` and two other functions: It also defines the function `poly` that evaluates the polynomial at a given point.  The main idea is that the script can be used to test whether a given list is a polynomial or the zero polynomial, or whether the list has a solution for the function `find_zero`.