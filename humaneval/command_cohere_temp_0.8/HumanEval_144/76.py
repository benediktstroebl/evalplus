```python
def simplify(x, n):
    num_x = map(int, x.split('/'))
    num_n = map(int, n.split('/'))
    return num_x[0] * num_n[0] % 1 == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into integers using `map()` and directly computes the product of the numerators and the product of the denominators to compare them modulo 1, which would evaluate to a whole number if both `x` and `n` are whole numbers. The function returns `True` if the product evaluates to a whole number and `False` otherwise.

Here is a simpler alternative approach using the `Fraction` class:
```python
def simplify(x, n):
    x, n = Fraction(x), Fraction(n)
    return x * n == int(x * n)
```

And here is a more efficient approach using the `operator` module:
```python
from operator import mul

def simplify(x, n):
    return str(x * n) == '1'
```

The tests for the given problem are:
```python
def test_simplify():
    assert simplify("1/5", "5/1") == True
    assert simplify("1/6", "2/1") == False
    assert simplify("7/10", "10/2") == False
```

The docstring of the function can be improved by adding more details about the expected input format:
```python
def simplify(x, n):
    """
    Simplify the expression x * n.
    Returns True if x * n evaluates to a whole number, and False otherwise.
    x and n are string representations of fractions in the format <numerator>/<denominator>.
    Both numerator and denominator are expected to be positive whole numbers, and denominators are not allowed to be zero.
    """
    x, n = Fraction(x), Fraction(n)
    return x * n == int(x * n)
```