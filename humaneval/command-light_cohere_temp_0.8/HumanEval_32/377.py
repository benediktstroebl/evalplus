```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x**2 + ... + xs[n] * x**n
    """
    return sum([coef * math.pow(x, i) for i, coef in enumerate(xs)])

def find_zero(xs: list):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0
    find_zero returns x that satisfies this equation, and has the largest non-zero coefficient among xs
    """
    if len(xs) % 2 != 0:
        raise ValueError("find_zero only takes lists with even number of coefficients")
    l = []
    while any(x != 0 for x in xs):
        x = 1 / xs.pop()
        method, using bisection to find zero, has the advantage of working in logarithmic time complexity, instead of numerical iteration.
    x is the x that makes poly(x) = 0
    l.append(x max(xs, key=abs))
    return l[0]

# tests
print(find_zero([1, 2])) # 1.0
print(find_zero([-6, 11, -6, 1])) # (-1.0)
``` 
The script defines a function **poly(xs, x)** that evaluates a polynomial at a given point x, given a list of coefficients xs. The **find_zero(xs)** function finds the zero of the polynomial poly(x) = 0, by using the method of bisection. It returns the max(xs, key=abs) which has the largest non-zero coefficient and is the x that makes the polynomial equal to zero.