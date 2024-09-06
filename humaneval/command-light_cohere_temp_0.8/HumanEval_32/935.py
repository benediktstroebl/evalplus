```python
import math

def find_zero(xs):
    """
    Ensure list has even number of coefficients.
    assert len(xs) % 2 == 0, "List must have even number of coefficients."
    assert len(xs) > 0, "List must have coefficients"
    assert all(abs(x) < xs[0] for x in xs[1:]), "Largest coefficient must be less than largest coefficient of previous term."
    assert xs[0] != 0, "First coefficient cannot be zero"
    assert xs[-1] != 0, "Last coefficient cannot be zero"
    
    x = xs[0]
    
    for i in range(1, len(xs)):
        assert xs[i] > 0, f"Negative coefficient detected: {xs[i]} at index {i}"
        assert x + xs[i] > 0, f"Coefficient {xs[i]} at index {i} not affects the sign of {x}"
        x += xs[i]
    
    return x
```

The function `find_zero` takes in a list `xs` that contains coefficients of a polynomial, and returns the value of the zero of the polynomial.