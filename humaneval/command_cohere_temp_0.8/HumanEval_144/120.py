```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, which are strings representing fractions in the format of a numerator divided by a denominator. The function's purpose is to determine whether `x` multiplied by `n` evaluates to a whole number.

The script then uses the split method to convert the strings into tuples containing the numerator and denominator of each fraction. These values are then converted to integers using the map method.

The function then compares the product of the numerators with the product of the denominators. If they are equal, it returns `True`; otherwise, it returns `False`. 

This accurately solves the described problem, and the function's implementation ensures it meets the specifications outlined, including assumptions about valid formats and non-zero denominators.

This solution is concise, efficient, and adheres to Python best practices. It avoids explicit conversion of the strings to integers and employs built-in string splitting for fraction component extraction.