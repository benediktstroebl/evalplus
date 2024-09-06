```python
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))
    return num1 * den2 == den1 * num2
```

This Python script defines a function `simplify` taking two arguments `x` and `n` as fractions in the format of a string `<numerator>/<denominator>`. The function splits the strings into integers and then computes the product of `num1` and `den2` as well as the product of `den1` and `num2` and compares the results, returning `True` if they are equal and `False` otherwise.

Here is a breakdown of the code:
- The lines `num1, den1 = map(int, x.split('/'))` and `num2, den2 = map(int, n.split('/'))` use the `map()` function to convert the numerator and denominator of the fractions to integers. The `split()` method is used to split the string representation of the fractions into two parts - the numerator and the denominator.
- The line `return num1 * den2 == den1 * num2` computes the product of the numerators and the product of the denominators and compares the results, returning `True` if they are equal and `False` otherwise. 

This solves the problem using a straightforward approach, checking if the product of the fractions evaluates to a whole number.