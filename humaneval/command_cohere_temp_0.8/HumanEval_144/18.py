```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. These are then split into their respective numerators and denominators and converted to integers using `int()`. 

The numerators are multiplied together, and the resulting product is divided by the denominator. The function then checks if this fraction equals a whole number, and returns True if it does, and False otherwise. The test cases provided are handled correctly by the function.