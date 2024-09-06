```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    return total * total == sq(a) + sq(b)

def sq(n):
    return n * n
```

The function `right_angle_triangle` checks whether the sum of the squares of sides a, b, and c is equal to the square of the total. If it is, this confirms that the triangle is right-angled. This approach leverages the Pythagoras theorem that states the square of the hypotenuse is equal to the sum of the squares of the other two sides.