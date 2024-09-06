```python
def derivative(xs: list) -> list:
    """ Returns the derivative of a polynomial represented by its coefficients xs. """
    result = [0] * (len(xs) - 1)
    x = 0
    for i in range(len(xs)):
        result[i] = xs[i+1] * (x + 1) - xs[i]
        x += 1
    return result
```

The tests cases are:
```python
>>> derivative([3, 1, 2, 4, 5])
[1, 4, 12, 20]
>>> derivative([1, 2, 3])
[2, 6]
>>> derivative([-5, 2, 3, 4, 5])
[-10, 4, 6, 8]
>>> derivative([12, -10, 4, 5, -6])
[36, -40, 20, -6]
```