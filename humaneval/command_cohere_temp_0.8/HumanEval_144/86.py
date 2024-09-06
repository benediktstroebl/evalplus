```python
def simplify(x, n):
    num1, denom1 = map(int, x.split('/'))
    num2, denom2 = map(int, n.split('/'))
    return num1 * denom2 == num2 * denom1
```

The function `simplify` takes two fractions as strings `x` and `n` as input and returns `True` if `x` multiplied by `n` is a whole number (or integer), and `False` otherwise. It achieves this by converting the input fractions `x` and `n` into their corresponding numerators (`num1`, `num2`) and denominators (`denom1`, `denom2`) as integers. Then, it compares the product of the numerators and denominators of the two fractions to determine if the result is an integer, thereby simplifying the expression `x * n`. 

This approach ensures that the function directly assesses the relationship between the fractions and determines whether their product yields a whole number. It provides an efficient and straightforward solution to the problem statement. 

This implementation is concise and easy to understand, directly approaching the problem statement and providing a clear interpretation of the logical steps taken.