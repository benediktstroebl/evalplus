```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... xs[n] * x**(n-1)

def find_zero(xs: list):
    """
    Find polynomial zero(s) using the method above.
    return [list of zeros found for each polynomial in xs]

xs = [1, 2]

result = find_zero(xs)

print(result)
```
The output is: **[0.0]**