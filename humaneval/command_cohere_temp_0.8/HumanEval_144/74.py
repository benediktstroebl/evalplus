```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n % den_n == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then calculates the product of the numerators and the remainder of this product divided by the denominator. The function returns `True` if this remainder is zero (i.e., the product simplifies to a whole number) and `False` otherwise.

This approach exploits the fact that, for any integer `a` and positive integers `b` and `c`, we have `a * b % c = 0` if `a % c = 0` and `b % c = 0`, and `a * b % c != 0` otherwise. Indeed, `x` and `n` are assumed to be fractions, so if their product simplifies to a whole number, they must both share a denominator, and likewise, their numerators must evenly multiply to each other. 

The script assumes that the input fractions are valid and do not have zero as the denominator, which is important to ensure that the division operation doesn't throw a `ZeroDivisionError` and that the result of the modulus operation is well-defined. 

This solution is succinct and computationally efficient, making it suitable for solving this problem.