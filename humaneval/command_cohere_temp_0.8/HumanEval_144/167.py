```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), [x, n])
    x, n = map(int, [x[0] * int(n[0]) / int(x[1]), n[1]])
    return x == round(x)
```

The function `simplify()` takes two fractions as input, represented as strings `x` and `n` and returns `True` if `x` multiplied by `n` is a whole number, and `False` otherwise. 

Here's how the function works:
- The fractions `x` and `n` are converted to integers using `map(lambda f: f.split('/'), [x, n])`. This splits each fraction string into a pair of integers representing the numerator and denominator. 
- The numerators are multiplied and the denominator is appropriately scaled using `x, n = map(int, [x[0] * int(n[0]) / int(x[1]), n[1]])`. 
- The resulting fraction is converted to a floating point number and rounded. It is then compared to the original integer value of `x` multiplied by `n` to determine whether the result is a whole number or not. 

The expected output of the function is:
```
True
False
False
```

The test cases are assumed to be provided in the same markdown code block as the problem statement.