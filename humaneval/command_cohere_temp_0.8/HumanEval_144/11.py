```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. These are then split into their numerator and denominator parts, and the resulting integers are used for calculation. 

The function ultimately returns True if `x * n` evaluates to a whole number and False otherwise. It achieves this by calculating the product of the numerators `num1 * num2` and the denominators `den1 * den2` separately, and then checking if the whole number `num1 * n / den1` equals the partial product of the numerators.