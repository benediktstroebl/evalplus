```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    return numx * denomn == numn * denomx
```

The function `simplify()` takes two fractions as string inputs represented in the format of a divide operation i.e. `numerator/denominator`. It splits the given strings into their respective numerators and denominators and converts them into integers using the `map()` function.

The function then performs a comparison of the product of the numerators and denominators of both fractions using the equality operator `==` to determine if the simplified expression of `x * n` results in a whole number or not.

The given examples in the problem statement will return the following values:
- `simplify("1/5", "5/1") = True`
- `simplify("1/6", "2/1") = False`
- `simplify("7/10", "10/2") = False`

This is because the first example's numerators and denominators are multiplied to give a whole number (1 * 5 = 5), whereas the second example's (1* 2 = 2) and the third example's (7 * 10 = 70) results are not whole numbers.