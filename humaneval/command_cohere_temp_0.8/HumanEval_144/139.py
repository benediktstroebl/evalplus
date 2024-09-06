```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    return num_x * num_n % den_n == 0 and num_x * den_n % den_n == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and converts them to integers for easier multiplication. The function then checks if the condition is met, wherein both `num_x * num_n % den_n == 0` and `num_x * den_n % den_n == 0` are evaluated to determine if the simplified expression evaluates to a whole number. The first condition checks if the product of the numerators is divisible by the denominator of the other fraction, and the second condition checks if the product of the denominator of the first fraction and the numerator of the second fraction is divisible by the denominator of the second fraction.