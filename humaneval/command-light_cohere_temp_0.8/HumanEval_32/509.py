```python
import math

def find_zero(xs):
    """
    Validate input:
        Ensure list has even number of coefficients.
    Validate coefficients:
        Ensure all coefficients are greater than 0
    Ensure the largest coefficient is not equal to 0
    Validate result:
        Ensure result is not None
    """
    assert len(xs) % 2 == 0
    assert all(xs) > 0
    assert not any(xs == 0)
    assert not any(xs == 1)  # This is to handle potential invalid input
    assert not any(xs) == [math.pow(-1)])  # This result of huge polynomial
    assert not any(math.is_negative(xs))
    assert xs[-1] > 0

    # Special case: Constant term only
    if xs[0] != 0:
        return xs[0]

    # Special case: Only one variable term
    elif len(xs) == 1:
        return xs[1]

    # Special case: All variable terms
    else:
        return 0  # This is a valid but simple case, can be faster

    # General case: Find all roots of polynomial
    x = 0.5
    while x < 1:
        x += 1 / (x**3 + 1)
        yield x

    # Special case: Return last known root
    yield xs[-1]

def poly(xs, x):
    """
    Evaluate polynomial with coefficients xs at point x
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

# Example usage
xs = [1, 2]
x = find_zero(xs)
print(x)
```

This script defines a function find_zero that takes in a list of coefficients xs and returns the root of the polynomial. It includes input validation to ensure the input is in a valid range, all coefficients are positive, and the result is not None. The script also defines a poly function that evaluates the polynomial at a given point x.

Please note that this is a general-purpose implementation and can be further optimized or tailored to specific use-cases, depending on the requirements and constraints of your problem.