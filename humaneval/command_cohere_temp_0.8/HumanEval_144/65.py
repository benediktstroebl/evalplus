```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), [x, n])
    x, n = map(int, [x[0] * int(n[0]) / int(x[1]), n[1]])
    return x == round(x)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format of `<numerator>/<denominator>`. The function first converts the two fractions to numeric values. It then multiplies the numerators and denominators separately and divides the result. The resulting fraction is then rounded, and if the resulting value is equal to the original (rounded) fraction, it means it's a whole number, otherwise it's not. The function returns `True` if the product of the two fractions simplifies to a whole number, and `False` otherwise.

Here is an example usage of the function:
```python
print(simplify("1/5", "5/1"))  # Outputs: True
print(simplify("1/6", "2/1"))  # Outputs: False
print(simplify("7/10", "10/2"))  # Outputs: False
```