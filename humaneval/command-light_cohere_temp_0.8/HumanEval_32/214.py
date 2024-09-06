```python
import math

def find_zero(xs):
    """xs are coefficients of a polynomial"""
    assert len(xs) % 2 == 0, "List must have an even number of coefficients"
    assert max(abs(xs)) > 0, "List must contain at least one nonzero coefficient"
    return [x for x in xs if x != 0]

def poly(xs, x):
    """
    Evaluate polynomial with coefficients xs at point x"""
    assert len(xs) > 0, "List of coefficients must be nonempty"
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def test_find_zero():
    try:
        xs = [1, 2]
        assert find_zero(xs) == [0.0, 0.5], "Lists't find zero for polynomial with coefficients [1, 2]"
        with xs:
            poly(xs, 1)
            assert poly(xs, 1) == 0, "Polynomial must be the zero"
            assert poly(xs, 2) != 0, "Polynomial must not be the zero"
    except:
        raise ValueError("tests failed")

test_find_zero()
```
The script defines three functions: `find_zero`, `poly`, and `test_find_zero`. The `find_zero` function finds the zero of a polynomial given by `xs`, and `poly` function evaluates a polynomial at a given `x`. The `test_find_zero` function contains test cases that validate the functionality of these functions. 

Note that the `find_zero` function and the test case `xs = [1, 2]`` are not valid because the list must have an even number of coefficients. This is's problem with a list of coefficients of polynomial is that the list should contain even number of elements.

This code can be used to verify the correctness of polynomial zero-finding algorithms.