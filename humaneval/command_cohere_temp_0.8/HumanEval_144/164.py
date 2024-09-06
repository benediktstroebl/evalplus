```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    return num_x * num_n % den_n == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then calculates the product of the numerators and the remainder of this product divided by the denominator. Then, it returns `True` if this remainder is zero, indicating that the product simplifies to a whole number, and `False` otherwise.

This implementation uses integer division (the `%` operator) to calculate the remainder, which is suitable for this problem since it's specifically asked to determine if the result is a whole number.