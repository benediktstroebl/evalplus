```python
def simplify(x, n):
    num_x, den_x = map(int, x.split('/'))
    num_n, den_n = map(int, n.split('/'))
    
    if den_x == 1:
        return num_n == 1
    elif den_n == 1:
        return num_x == 1
    else:
        return num_x * num_n == den_x * den_n
```

The function `simplify` takes in two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. The function splits each string into their respective numerators and denominators and then checks a few conditions:
- If `denominator_x` is 1, it returns `true` if `numerator_n` is 1, simplifying `x * n` to a whole number.
- If `denominator_n` is 1, it returns `true` if `numerator_x` is 1, simplifying `x * n` to a whole number.
- If neither denominator is 1, it checks if the product of numerators equals the product of denominators, indicating whether `x * n` simplifies to a whole number or not.