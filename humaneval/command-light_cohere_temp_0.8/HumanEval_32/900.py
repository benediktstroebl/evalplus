```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + .... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that the polynomial is zero,
    find_zero returns only zero point, even if there are many solutions
    """
    # make sure coefficients list has even number of elements
    assert len(xs) % 2 == 0
    assert len(xs) > 1

    # sort coefficients to ensure that larger coefficients are always in front
    xs.sort(xs, key=lambda x: x[0])
    xs.sort(xs, key=lambda x: x[1])

    # initialize the result with x**n
    result = x**len(xs)

    # initialize the j to j = 0, and loop until the value of j is less than len(xs)
    for j in range(len(xs)):
        # multiply x**j by result and add current coefficient
        result = result * x**j + xs[j]
        # j is incremented by 1
        j += 1

    # return the result
    return result


xs = [1, 2]
x = 2.0
result = find_zero(xs)
print("result =", result)
``` 
This Python code defines a function `find_zero` that finds the zero of a polynomial represented by a list of coefficients `xs`. The function first ensures that the list of coefficients has an even number of elements, then sorts the coefficients in descending order based on their magnitudes. The function then initializes the polynomial with `x**n` and iteratively adds the current coefficient to the result while multiplying by `x`. Finally, the function returns the result, which represents the value of the polynomial at the point `x`.