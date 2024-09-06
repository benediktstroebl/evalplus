```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    if numx * denomn == denomx * numn:
        return True
    else: 
        return False
```

This function takes two fractions as input, x and n, and returns True if the product of these two fractions is an integer, and False otherwise. It splits the input fractions into their numerators and denominators as integers and then checks if the product of the numerators is equal to the product of the denominators to determine if the expression simplifies to an integer or not.