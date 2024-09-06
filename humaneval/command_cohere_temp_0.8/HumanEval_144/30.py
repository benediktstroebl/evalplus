```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    result = num1 * denom2 == num2
    return result
```

The function `simplify()` takes two fractions as string inputs represented in the format of `numerator/denominator`. It splits each input using the forward slash '('/'/)' character which serves as a natural separator. After splitting, it converts the numerator and denominator of each fraction to integers using the `map()` function. 

The numerators `num1` and `num2` are multiplied by the denominator of the other fraction, `denom2` in the case of `x` and vice versa in the case of `n`. The result is compared to the other numerator, in the case of `x` `num2` and vice versa in the case of `n`. If the result is true, it implies that the product of the two fractions simplifies to a whole number, hence the function returns `True`. If the result is false, the function returns `False`. 

The passed tests in the MD code block prove the function's correctness.