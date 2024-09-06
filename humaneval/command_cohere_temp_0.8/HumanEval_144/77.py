```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 and denom1 * num2 == denom2
```

The function `simplify()` takes two fractions as input, `x` and `n`, and returns `True` if `x` multiplied by `n` is a whole number, and `False` otherwise. It achieves this by first converting the input fractions `x` and `n` into their respective numerators and denominators as integers using `int(x.split('/'))`. It then compares the product of the numerators and denominators of the two fractions to determine if the result of multiplying the two fractions would be a whole number. The result is then returned as either `True` or `False`. 

This algorithm is encapsulated in a standalone function, making it easily reusable and testable.