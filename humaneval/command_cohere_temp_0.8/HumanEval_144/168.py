```python
def simplify(x, n):
    numx, denomx = map(int, x.split('/'))
    numn, denomn = map(int, n.split('/'))
    reciprocal = denomx * denomn
    return (numx * numn % reciprocal == 0)
```

The function `simplify()` takes two fractions as input, `x` and `n`, and returns `True` if `x` multiplied by `n` is a whole number, and `False` otherwise. 

Here's how the function works: 
 1. It splits each fraction input into two numbers - the numerator and the denominator using the `split('/')` method. 
 2. It then takes the numerator of x and multiplies it by the numerator of n, taking the modulus with the product of the denominators. It checks if this result is 0, which would indicate that the expression x*n is a whole number. 

The given test cases pass with this implementation. You can verify this by importing the function and running the tests:
```python
import simplify 

# Test cases
print(simplify.simplify("1/5", "5/1")) # Output: True
print(simplify.simplify("1/6", "2/1")) # Output: False
print(simplify.simplify("7/10", "10/2")) # Output: False
``` 
You can also add additional test cases to ensure the function handles edge cases and corner cases.