```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify()` takes two fractions as input, represented as strings `x` and `n`. It splits each fraction into a numerator and a denominator, then converts these parts to integers using `map(int, ...)`. Then, to determine if the product of the two fractions simplifies to a whole number, it compares the product of the numerators with the product of the denomiers. If they are equal, the function returns `True`; otherwise, it returns `False`.