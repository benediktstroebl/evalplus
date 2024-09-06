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
    Finds a solution x for polynomial coefficients coefficients such that f(x) = 0.
    Returns only one solution, even in case of multiple zeros.
    Works only for lists of coefficients with even length and non-zero coefficients.
    """
    # Make sure list of coefficients has even length and highest coefficient is not zero
    if len(coefficients) % 2 == 1 or coefficients[0] == 0:
        raise ValueError("List of coefficients should have even length and be non-zero")
    
    # Calculate polynomial result for x = 0
    y0 = poly(coefficients, 0)
    
    # Divide polynomial into pairs of coefficients,
    # e.g. [2,3] => [2,-3]
    coefficients = [-coeff for coeff in coefficients[1:-1]]
    
    # and reverse order of coefficients, so we can use binary search
    # x = -b/2 ... means we need to evaluate polynomial at x = -b/2,
    # and check if result is equal to 0
    return binary_search(-coefficients[0] / 2)


def binary_search(x: float) -> float:
    """
    Does binary search to find solution for polynomial.
    Starts search from middle of search space,
    and does division in half each time,
    returning result of evaluation of polynomial at result.
    """
    def get_middle(l):
        return l[:len(l) // 2]

    def divide(l):
        return [x for i in range(len(l) // 2)]

    def check(l, x):
        return poly(l, x) == 0

    while True:
        middle = get_middle(divide(coefficients))
        x_mid = -middle[0] / 2

        if check(middle, x_mid):
            return x_mid

        # If polynomial evaluation is positive,
        # we need to search in left part of interval
        if poly(middle, x_mid) > 0:
            coefficients = divide(middle)
        # If polynomial evaluation is negative,
        # we need to search in right part of interval
        else:
            t = [-(-x_mid - 1) / 2 for _ in middle]
            coefficients = [t[i] if i % 2 else -t[i] for i in range(len(t))]

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
```

This code includes a `poly` function, which evaluates a polynomial given its coefficients and a variable point, and a `find_zero` function that finds the zero value of a polynomial. The `find_zero` function pre-processes the coefficients to ensure that it has an even number of coefficients and that the coefficient list is not zero. It then performs a binary search by evaluating the polynomial at the midpoint of two polynomial coefficients. If the value is zero, it has found the solution. If the value is greater than zero, it modifies the coefficients to search the left half of the interval. Otherwise, it modifies the coefficients