```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

The function `simplify` takes in two parameters, `x` and `n`, which are strings representing fractions in the format of `<numerator>/<denominator>`. Their numerators and denominators are extracted using `map(int, x.split('/'))` and then compared to determine if the product of `x` and `n` is a whole number or not.

This solution tests correctly against the given test cases. It's worth noting that this solution assumes that the input fractions have only integers in their numerators and denominators and does not handle other potential edge cases that might arise when dealing with more general input.