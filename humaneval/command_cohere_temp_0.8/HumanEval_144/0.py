```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == int(num1 * n / denom1)
```

This Python script defines a function `simplify` taking two arguments `x` and `n`, where both `x` and `n` are string representations of fractions in the format of `<numerator>/<denominator>`. This function's purpose is to determine whether `x * n` evaluates to a whole number or not. 

The function uses `split()` to separate the numerator and denominator of both fractions. Then uses `map()` to convert these strings to integers. Finally, it compares the numerator multiplied by the denominator of n with the result of evaluating `x * n` as a fraction to determine if the result is a whole number or not. It returns `True` if it is and `False` otherwise. This solution relies on the assumption that both inputs are valid fractions and do not have zero as a denominator.

This solution can be improved by asking for input validation to ensure that the input follows the expected format and that the denominator is not zero, thereby avoiding potential errors and providing more robust handling. 
Here is a simpler alternative solution using python:
```python
def simplify(x, y):
    return str(x) + ' '*y == str(int(x)*int(y))
```
In this solution, we take advantage of the fact that we can concatenate strings in python with the `+` operator, and that we can pass the resulting string to the `int` function which will evaluate it if possible. Therefore we can simply compare the concatenation of the numerator and denominator of the result with the concatenation of the numerator and the number of times the denominator of y should be multiplied by.