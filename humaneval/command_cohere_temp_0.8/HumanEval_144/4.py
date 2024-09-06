```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. The function splits each string into respective numerator and denominator values and then compares the product of the numerator and denominator of one fraction against the other and returns a boolean indicating whether the product evaluates to a whole number.

Here is a simpler solution using python's built-in functions (`int`, `split` and `product`) and arithmetic operations:
```python
def simplify(x, n):
    return int(x.split('/')[0] * n.split('/')[1]) == int(x.split('/')[1] * n.split('/')[0])
```

The above solution directly compares the products of numerators and denominators of the two fractions.