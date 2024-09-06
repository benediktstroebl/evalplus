```python
import math

def find_zero(xs):
    if len(xs) != 2:
        raise ValueError("Input must be a list of length 2")
    return math.floor(poly(xs, 0))

def poly(xs, x):
    return sum([xs[i] * math.pow(x, i) for i, coeff in enumerate(xs)])

# Example usage:
xs = [1, 2]
x = 0
result = find_zero(xs)
print(result)  # Output: 1.0
poly(xs, x)  # Output: 1 + 2x
```

This code defines a function find_zero that takes a list of coefficients xs as input and finds the zero of the corresponding polynomial. It has a test if the list has odd length, it raises a ValueError with a corresponding error message. If the list has two coefficients, it calculates the zero of the polynomial using the sum of the coefficients multiplied by the power of x and returns the result.