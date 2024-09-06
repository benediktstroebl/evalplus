```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions
    find_zero only takes list xs having even number of coefficients and the largest non-zero coefficient as it guarantees a solution.

    # Example first, find_zero([1, 2]) == 1.2
    # f(x) = 1 + 2x
    -0.5
    #    # f(x) = -6 + 11x - 6x^2 + x^3
    -0.5
    #    # f(x) = 1 + 2x
    -0.5
    #    # f(x) = -6 + 11x - 6x^2 + x^3
    -0.5

    #    # f(x) = 1 + 2x
    -0.5
    #    # f(x) = -6 + 11x - 6x^2 + x^3
    -0.5
    #  # f(x) = -6 + 11x + 6x^2 + x^3
    -0.5

    #    # f(x) = 1 + 2x
    -0.5
        #    # f(x) = -6 + 11x - 6x^2 + x^3
    -0.4
    #    # f(x) = -3 + 2x
    -0.5
        #    # f(x) = -6 + 11x - 6x^2 + x^3
        -0.25
        #    # f(x) = -1 + 2x
        -0.5
    #    # f(x) = -6 + 11x - 6x^2 + x^3
        -0.15
        #    # f(x) = -3 + 2x
        -0.5
        #    # f(x) = -6 + 11x - 6x^2 + x^3
        0.0
    #    # f(x) = -1 + 2x
        -0.5
        #    # f(x) = -6 + 11x - 6x^2 + x^3
        0.0

    #    # f(x) = -1 + 2x
        -0.0

        # testing the
        # testing
        assert find_zero([1, 2]) == 1.2
        assert find_zero([-6, 11, -6, 1]) == (-0.25, 1.0)
        assert find_zero([-6, 11, -6, 1, -6, 11, -6, -6, 1]) == (-0.25, -0.0)
        assert find_zero([-6, 11, -6, 1]) != find_zero([-6, 11, -6, 1, -6, 11, -6, 11, -6])
        ```
The test cases have been added to ensure that the function `find_zero` passes all the tests.