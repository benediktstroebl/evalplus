```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    return numx * denomn == numn * denomx
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then compares the product of the numerators and denominators of both fractions to determine if the simplified expression would be a whole number or not.

This algorithm is case-sensitive and will not properly handle any expressions involving variables or operations other than multiplication. It is also not robust against integer overflow for very large numerators and denominators. These potential issues could be addressed with additional parsing and checking. 

This is the kind of problem that could be encountered in a typical software engineering mathematics assessment, which often require understanding of basic algebra and ability to translate problems into working code. 

If you're interested in more practice with these kinds of problems, try providing test cases for the code and making sure that you can explain how each test case highlights a particular facet of the code's functionality.