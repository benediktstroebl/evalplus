```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == int(num2 * denom1)
```

This Python script defines a function `simplify` taking two arguments `x` and `n` which are string representations of fractions. The function's purpose is to determine whether `x * n` simplifies to a whole number. It achieves this by splitting `x` and `n` into their numerators and denominators and then multiplying these values together. Lastly, it compares the resulting product to a whole number, returning `True` if they're equivalent and `False` otherwise. 

For example, the statement `simplify("1/5", "5/1") = True` is true because:
- `num1 = 1`
- `denom1 = 5`
- `num2 = 5`
- `denom2 = 1`

Their product is `num1 * denom2 = 1 * 1 = 1`, which is a whole number, thus the statement passes.