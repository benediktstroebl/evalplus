```python
import math
def find_or_compute_zero(xs: list):
    if len(xs) % 2 == 0:
        return math.poly(xs[0]) + math.pow(xs[1]) * math.pow(xs[2]) + ... * math.pow(xs[len -
    return None
    elif len(xs) == 1:
        return xs[0]
    else:
        return find_or_compute_zero(xs[:-])
def polynomial_eval(xs: list):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
def find_zero(xs: list):
    x = xs[0]
    for coef in xs[1:]:
        x = math.pow(x, x) * coef
    return x
result = find_or_compute_zero([1, 2])
print(result) # should print 2
result = find_zero([1, 2])
print(result) # should print 2
``` 
The code defines a set of functions to evaluate polynomial, find the zero of polynomial and compute the zero of a polynomial.