```python
def simplify(x, n):
    x, n = map(lambda f: f.split('/'), (x, n))
    return int(x[0] * n[0]) % 1 == 0 and int(x[1] * n[1]) % 1 == 0
```

The spec explicitly states that the numerators and denominators are whole numbers, so we can simplify the equation `x * n` to `numerator(x) * numerator(n) / denominator(x) / denominator(n)`.

Therefore, if both numerators and denominators (when taken as whole numbers) produce integers when multiplied together, then the answer is a whole number, otherwise it's not.

This can be done via Python's built-in `int` function, which will automatically up-cast (via overflow) any decimal numbers to integers.

We simply need to check if the resultant integer is a multiple of 1 (which it will be if it's an entire number) via the modulus operator.

This is then directly returned as a boolean value.