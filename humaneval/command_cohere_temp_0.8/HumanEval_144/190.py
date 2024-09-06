```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    return num_x * num_n == den_x * den_n
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits each string into two integers (`num_x, den_x`) and (`num_n, den_n`) for the numerator and denominator, respectively. Then, it compares the product of the numerators with the product of the denominators to determine if the simplified expression evaluates to a whole number or not.

This solution assumes that the input fractions have valid formats and that the denominators are not zero, as stated in the problem statement.