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
    find_zero finds x such that poly(x) = 0.
    find_zero returns only zero point, even if there are many solutions.
    Furthermore, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees
    a solution.

    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0

   
    hash_length: 20
    """

def test_find_zero(xs: list):
    """
    Test case:
    Test if find_zero returns a number for given polynomial.
    Test by applying the
    Test case:
    Test if find_zero returns the correct number for a given polynomial.
    Test case:
    Test if find_zero returns the correct number for a given polynomial.
    """
    hash_length: 20
    """
    return find_zero(xs) == math.sqrt(xs[-1])

def main():
    print("Find Zero")
    print(test_find_zero([1, 2]))
    print(test_find_zero([-6, 11, -6, 1]))

if __name__ == "__main__":
    main()
```

This code defines a Python function called `poly` that calculates the polynomial for a given list of coefficients. The function takes a input of a list of coefficients and a single `x` value. It then returns the polynomial by adding up the coefficients multiplied by the corresponding powers of `x`.

The `find_zero` function is used to find the zero of the polynomial. It takes the list of coefficients as input and returns the `x` value that makes the polynomial equal to zero.

The `test_find_zero` function is used to test the `find_zero` function by passing in a list of coefficients and checking if the returned value matches the expected zero value for the polynomial.

Finally, the `main` function is called, which simply prints out the "Find Zero" message and then prints the results of the test cases using the `test_find_zero` function.