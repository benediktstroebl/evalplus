```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    x, n = map(int, (x, n))
    return n % 1 == 0
```

The approach used to solve the problem is:
- It splits the numerator and denominator of the fractions and then converts them to integers.
- It then returns `True` if `n` (product of the numerators) is divisible by 1 (a whole number), and `False` otherwise.