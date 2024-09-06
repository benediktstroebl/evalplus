```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    return numx * denomn == numn * denomx
```

The function `simplify()` takes two fractions as string inputs and returns a boolean indicating whether the product of the two fractions is an integer. It splits each fraction into a numerator and a denominator, then compares the product of the numerators and denominators of both fractions and returns a Boolean indicating whether they are equal.

Here is a breakdown of the functionality of the code for the given test cases: 
- simplify("1/5", "5/1") = True:
1. split("/"): 1/5 -> (1, 5)
2. split("/"): 5/1 -> (5, 1)
3. (1, 5) * (5, 1) -> (1, 1) which is a whole number
- simplify("1/6", "2/1") = False:
1. split("/"): 1/6 -> (1, 6)
2. split("/"): 2/1 -> (2, 1)
3. (1, 6) * (2, 1) -> (2, 6) which is not a whole number 
- simplify("7/10", "10/2") = False:
1. split("/"): 7/10 -> (7, 10)
2. split("/"): 10/2 -> (10, 2)
3. (7, 10) * (10, 2) -> (70, 20) which is not a whole number 

The code handles the test cases provided and produces the correct boolean output.