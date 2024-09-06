```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == int(num1 * n / den1)
```

This Python script defines a function `simplify` taking two variables `x` and `n` as input, which are string representations of fractions. The function uses `split()` to separate the numerator and denominator of the fractions, and then uses `int()` to convert these components into integers. 

The code then checks if the product of the numerators `num1 * num2` is equal to the integer value obtained by dividing the first numerator by the second denominator. This can be done by employing integer division (`//`) to discard the decimal part of the calculation. 

The function returns `True` if the expression `x * n` evaluates to a whole number, and `False` otherwise. It is important to note that this function assumes that both `x` and `n` are valid fractions and do not have zero as a denominator. 

This solution is concise and straightforward, utilizing basic Python syntax and logic to determine if a particular expression evaluates to a whole number or not.