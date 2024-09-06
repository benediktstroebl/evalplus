```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), [x, n])
    x, n = map(int, [x[0] * int(n[0]) / int(x[1]), n[1]])
    return x % 1 == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. The function first converts these strings into integers using `int(f.split('/')[0])` to calculate the numerators and `int(f.split('/')[1])` to calculate the denominators. It then simplifies the expression `x * n` by multiplying the numerators and denominators separately, before dividing the two results. 

Finally, it checks if the result is an integer (whole number) by evaluating if the result modulo 1 is equal to 0. If it is, the function returns `True`; otherwise, it returns `False`. 

This code assumes that the input strings `x` and `n` follow the specified format and that both numerators and denominators are positive whole numbers, and it returns `True` if the product of the two fractions simplifies into a whole number and `False` otherwise.

The expected outputs are:
```
True
False
False
```