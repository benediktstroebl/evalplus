```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. Using the built-in function `map()` which applies a given function to each item of a specified collection (e.g., a list or an array), it extracts the numerator and denominator of each fraction. Afterward, the function checks whether the product of the second fraction's numerator and the first fraction's denominator is equal to the product of the first fraction's numerator and the second fraction's denominator. If they are equal, it returns `True`; otherwise, it returns `False`.

The expected output of the provided test cases is:
```
True
False
False
```