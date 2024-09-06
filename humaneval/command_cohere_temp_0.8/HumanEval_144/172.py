```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    x, n = map(int, (x, n))
    return n % 1 == 0
```

The approach used to solve the problem is to take two integers represented as strings in the format `numerator/denominator` and evaluate their product taken as a floating point number. The function then returns `True` if that number is an integer (whole number) and `False` otherwise.

It is important to note that this solution assumes that the inputs are valid fractions and do not have a zero in the denominator as mentioned in the original problem. If those assumptions were not made, further validation would be necessary.