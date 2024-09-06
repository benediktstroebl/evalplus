```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    if numx * denomn == numn * denomx:
        return True
    else: 
        return False
```

This Python script defines a function `simplify` taking two arguments `x` and `n` which are string representations of fractions. The function's purpose is to determine whether `x * n` simplifies to a whole number. It achieves this by splitting `x` and `n` into their respective numerators and denominators as integers using the `map` function. Subsequently, the function compares the product of the numerators and denominators of both fractions. If they are equal, it returns `True`; otherwise, it returns `False`. 

This algorithm is designed to accommodate valid fractions with positive whole number components and does not involve any divisions, hence efficiently executing the simplification assessment.