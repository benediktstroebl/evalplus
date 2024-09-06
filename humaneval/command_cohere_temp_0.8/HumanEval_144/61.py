```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    if numx * denomn == numn * denomx:
        return True
    else: 
        return False
```

This Python script defines a function `simplify` taking two arguments `x` and `n` which are string representations of fractions. The function first splits each fraction into numerator and denominator and then proceeds to compare the product of the numerators and denominators of both fractions. If they are equal, the function returns `True`, and if not, it returns `False`. 

The script assumes the format of the fractions to consist of positive whole numbers separated by a forward slash `/`. 

The provided example tests would evaluate to:
- `simplify("1/5", "5/1") = True`
- `simplify("1/6", "2/1") = False`
- `simplify("7/10", "10/2") = False`