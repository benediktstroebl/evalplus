```python
import math
def poly(xs):
    """
    Evaluates polynomial with coefficients xs at point x,
    returns sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs):
    """
    xs are coefficients of a polynomial
    find_zero find x such that poly(x) = 0,
    finds only zero point, even if there are many,
    finds only list xs having even number of coefficients and largest non zero coefficient guarantees solution
    """
    return [x for x in [x for x in xs if not poly(x)]]
# run test with following list of coefficients
xs = [1, 2, -0.5, -6]
ans = find_zero(xs)
print("find_zero :", ans)
print("poly :", poly(xs))
```
The function `find_zero` finds the zero of a polynomial represented by the list `xs` by using a list comprehension. The function returns a list of the only x-values for which the polynomial evaluates to zero. 

The function `poly` evaluates the polynomial represented by the list `xs` at the point `x` by using the `sum` function to calculate the sum of the product of each coefficient multiplied by `math.pow(x, i)` for each term of the polynomial.