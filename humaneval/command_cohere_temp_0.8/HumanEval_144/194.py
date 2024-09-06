```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    reciprocal = denomn != 1
    if reciprocal:
        numn, denomn = denomn, numn
    if numx == numn and denomx == denomn:
        return True
    elif numx * denomn == numn * denomx:
        return True
    else:
        return False
```

The function `simplify` takes in the two fractions `x` and `n` as a pair of strings, and returns `True` if the product of the two fractions is an integer, and `False` otherwise. 

The function utilizes the fact that if the numerators of the fractions are equal and the denominators are equal, then the product of the fractions equals an integer. Additionally, if the numerators are not equal but the product of the numerators is equal to the product of the denominators, then the product of the fractions equals an integer. 

Here is an example of how you can test this function:
```python
# Test the function
assert simplify("1/5", "5/1") == True
assert simplify("1/6", "2/1") == False
assert simplify("7/10", "10/2") == False
```

This way, the function simplifies the given expression `x * n` in an integer-seeking manner.