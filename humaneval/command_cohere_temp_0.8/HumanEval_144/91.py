```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    x, n = map(int, (x, n))
    return n % 1 == 0 and x % 1 == 0
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format of `'numerator/denominator'`. It splits each fraction into its numerator and denominator and then converts these numerators and denominators to integers using `map(int,)`. 

The function then checks if both integers evaluate to whole numbers when divided by 1 (i.e., if `n % 1 == 0` and `x % 1 == 0` hold true). If this condition is true, it returns `True`; otherwise, it returns `False`. 

This solution adheres to the given assumption that both `x` and `n` are valid fractions without zero in their denominators, as specified in the problem statement. 

This approach ensures that the function directly returns a boolean value without the need for any intermediate variables, thereby maintaining brevity and efficiency in its implementation.