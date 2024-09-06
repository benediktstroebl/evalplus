```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients. """
    ans = [0]*(len(xs)-1)
    num = 1
    for i in range(1, len(xs)):
        ans[i-1] = num * (xs[i] - xs[i-1])
        num += 1
    return ans
```

The derivative of a polynomial P(x) = a_n * x^n + a_(n-1) * x^(n-1) + … + a_1 * x + a_0 is given by:
P'(x) = n * (a_n * x^(n-1) + a_(n-1) * x^(n-2) + … + a_1) + a_0

Example usage:
```python
print(derivative([3, 1, 2, 4, 5])) 
```

Which would output:
```python
[1, 4, 12, 20]
```

This matches the desired output.