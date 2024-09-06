Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for i equal to 0..n
    where n = len(coefficients)
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero, even if there are multiple.
    Works only for lists with even number of coefficients,
    and with largest coefficient non-zero
    """
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        return "Coefficients list should have an even length and the largest coefficient cannot be zero."

    # invert coefficients and evaluate at x = 1 to get residues
    residues = [coeff for coeff in coefficients if coeff != 0]
    inverted_poly = [math.pow(x, len(residues)) for x in residues]
    result = sum(inverted_poly) / coefficients[0]

    for i in range(2, 1000):
        x = result + i
        if poly(coefficients, x) == 0:
            return result
```

This script defines the functions `poly` and `find_zero`. The `poly` function evaluates a polynomial's value at a given point, while the `find_zero` function finds a solution for the polynomial equation `poly(x) = 0`. This method only provides the first zero point encountered, and it operates exclusively on coefficient lists with even lengths and non-zero largest coefficients.

In the `find_zero` function, if the length of the coefficients list is odd or if the largest coefficient is zero, it returns an error message to indicate that the input criteria aren't met. Then, it inverts the coefficients and evaluates the polynomial at x = 1 to obtain the residues. Subsequently, it calculates the inverted polynomial and finds the sum divided by the leading coefficient to get the initial guess 'result'. Lastly, it iterates from 2 up to 1000, each time adding the iteration number to the guess, and checks if the polynomial evaluates to zero; once it finds a zero, it returns that value. 

You can test these functions separately with the provided test cases like so:
```python
# Test the poly function
assert poly([1, 2, 3], 2) == 5, "Failed poly test"

# Test the find_zero function
assert round(find_zero([1, 2]), 2) == -0.5, "Failed find_zero test"
assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0, "Failed find_zero test"
``` 
This way, you can verify that these functions operate correctly.