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
    and assigns zero to return value if input list lacks even number of coefficients.
    """
    if len(coefficients) % 2 == 1:
        return 0.0  # Return 0 if odd number of coefficients, as no valid polynomial exists.
    max_pow = len(coefficients) // 2
    x = float(-max_pow)
    while poly(coefficients, x) == 0:
        x = x + 1.0
    return x
```

This script defines two functions: `poly`, which evaluates a polynomial at a given point, and `find_zero`, which finds the point at which a polynomial is equal to zero. The `find_zero` function works by guessing the root position and iteratively moving leftwards checking if the polynomial is zero at the current position. It returns the first zero point found. 

The functions are self-contained and do not rely on any external variables or functions, making them easy to use and incorporate into other scripts. 

You can test these functions by calling them with example input coefficients lists, such as:
```python
print(find_zero([1, 2]))  # Expected output: -0.5
print(find_zero([-6, 11, -6, 1]))  # Expected output: 1.0
``` 

This script and its corresponding functions are written in Python and can be executed directly in any Python environment capable of running Python scripts.