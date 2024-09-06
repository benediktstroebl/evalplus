Here's a Python script that includes a function to solve the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients xs at point x.
    Returns sum of terms where each term is coefficient multiplied by corresponding x^i, for i from 0 to n.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Only returns the first solution found.
    
    Criteria for validating a set of coefficients:
    - Number of coefficients should be even.
    - Largest coefficient should be non-zero.
    """
    n = len(coefficients)
    if n % 2:
        raise ValueError('Coefficients list must have an even length.')
    if coefficients[-1] == 0:
        raise ValueError('Largest coefficient must be non-zero.')
    
    # Calculate differences between subsequent coefficients
    differences = [coefficients[i+1] - coefficients[i] for i in range(n // 2)]
    
    # Use the constant difference method to find a zero
    diff_count = len(set(differences))
    if diff_count == 1:
        # Handle the case where all differences are the same
        return (-differences[0] / (2 * coefficients[n // 2])) % 1
    elif diff_count > 2:
        # Handle the case where there are multiple differences
        # Find the gap between the difference sequence and the sequence of multiples of the fundamental difference
        fundamental_diff = differences[0]
        for i in range(1, len(differences)):
            if differences[i] != fundamental_diff * (i + 1):
                gap = fundamental_diff * (i + 1) - differences[i]
                break
        return (gap / (2 * coefficients[n // 2])) % 1
    else:
        # Handle the case where there are no real roots (difference sequence is empty)
        return 0
```

This script includes two functions. The first function, `poly`, takes a list of coefficients and a value `x` as input and returns the value of the polynomial at `x`. The second function, `find_zero`, takes a list of coefficients as input and returns the value of `x` at which the polynomial evaluates to zero, if such an `x` exists. This function only returns the first zero it finds. The functions are designed to handle any polynomial with even a number of coefficients and a non-zero leading coefficient. 

The `find_zero` function uses a basic technique to find a zero of the polynomial. The technique exploits the fact that if `n` is the degree of the polynomial, then `n+1` is the maximum number of factors of the polynomial. The basic idea is to:
1. Compute the differences between subsequent coefficients.
2. If there are `n+1` unique differences, then this is the maximum number of roots.
3. If there are more than `n+1` unique differences, then there are no roots.
4. If there are `n+1` unique differences, then the `i`th difference is proportional to the `i`th root.
5. Compute the proportionality factor and return it as the `i`th root.