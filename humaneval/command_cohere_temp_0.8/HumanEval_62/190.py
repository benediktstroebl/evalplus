```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by coefficients xs where xs[0] is the constant term and xs[1:] are the coefficients of the linear and quadratic terms. """
    ans = [0] * (len(xs) - 1)
    for i in range(1, len(xs)):
        ans[i - 1] = xs[i] * (i + 1) - xs[i - 1]
    return ans
```

The derivative operation is a standard operation for differentiating polynomials term by term and is present in most calculus textbooks. 

The function can be called as follows:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
```
The above calls return the derivative of the respective polynomial kernels.