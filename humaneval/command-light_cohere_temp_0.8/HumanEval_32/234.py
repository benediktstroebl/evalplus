```python
import math
def poly(xs):
    return sum([coef * math.pow(x) for x, coef in zip(xs, math.stars(x for x in range(len(xs)))))
def find_zero(xs):
    # tests if there is a single root
    root = float('-inf')
    for x in range(len(xs)):
        if xs[x] != 0:
            root = max(root, x)
    return root
xs = [1, 2] # coefficients of a polynomial
x = find_zero(xs) # find root
print("Root is:", x)
```