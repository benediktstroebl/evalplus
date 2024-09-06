```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    return numx * denomn == numn * denomx
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. They are split into integers `numx`, `denomx`, and `numn`, `denomn` respectively. The function then compares `numx` multiplied by `denomn` to `numn` multiplied by `denomx` and returns a boolean indicating whether they are equal, hence evaluating the expression `x * n`.

This solution relies on Python's built-in functionalities to convert strings to integers and perform arithmetic operations on those numbers. 

This problem can also be solved using Python's `fractions` library, providing a slightly different interface to achieve the same goal:
```python
from fractions import Fraction

def simplify(x, n):
    x = Fraction(x)
    n = Fraction(n)
    return x * n == Fraction(n.numerator * x.denominator, x.numerator * n.denominator)
```

This alternative function leverages the `Fraction` class from the `fractions` library to convert the strings `x` and `n` into fraction objects. The expression is then simplified using the `*` operator, and the resulting fraction object is compared to the truthy fraction created from the simplified expression.

Both provided approaches yield the same solution and may vary in efficiency and readability depending on the context. 

The first method uses Python's built-in numeric capabilities to achieve the desired result, while the second option leverages the `fractions` library for direct fractional manipulation. 

Regardless of preference, the chosen method should be applied uniformly and consistently to achieve the intended purpose.