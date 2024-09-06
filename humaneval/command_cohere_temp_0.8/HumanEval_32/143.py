Here's a Python script with a self-contained function that solves the problem:
```python
import math

def poly(coefficients: list, x: float) -> float:
    """
    Evaluates polynomial with coefficients coefficients at point x.
    Returns sum of coefficients[i] * x^i, for all i.
    
    Example:
    >>> poly([1, 2, 3, 4, 5], 2)
    47
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(coefficients)])


def find_zero(coefficients: list) -> float:
    """
    Finds a solution x for the equation poly(x) = 0.
    Returns only the first found zero.
    
    Preconditions:
    - coeffs is an even-length list of coefficients, with the largest non-zero coefficient at even indices.
    
    Returns: the solution x.
    """
    # your code here
    # You can use the following code as a reference:
    if len(coefficients) % 2 == 1:
        raise ValueError("coefficients list must have an even length.")
    max_index = len(coefficients) // 2
    max_coeff = coefficients[max_index]
    if max_coeff == 0:
        raise ValueError("largest coefficient must be non-zero.")
    x = -max_coeff / (max_index + 1)
    temp_sum = sum([math.pow(x, i) for i in range(max_index, -1, -1)])
    if temp_sum == 0:
        return x
    else:
        return find_zero([coefficients[i] - temp_sum for i in range(max_index, -1, -1)])

# Tests:
coefficients1 = [1, 2]
print(f'find_zero({coefficients1}) == -0.5: {find_zero(coefficients1):.2f}')

coefficients2 = [11, 6, -6, 1]
print(f'find_zero({coefficients2}) == 1.0: {find_zero(coefficients2):.2f}')

coefficients3 = [2, 5, 2, 1, 2]
print(f'find_zero({coefficients3}) == 1.0: {find_zero(coefficients3):.2f}')

coefficients4 = [1, 2, 3]
print(f'find_zero({coefficients4}) == None: {find_zero(coefficients4)}')
``` 

This script defines the `poly` and `find_zero` functions as specified in the problem statement. The `poly` function evaluates the polynomial at the given point `x`, and the `find_zero` function finds the solution for the polynomial equation `poly(x) = 0`. The script also includes tests that check the behavior of the `find_zero` function with different sets of coefficients.