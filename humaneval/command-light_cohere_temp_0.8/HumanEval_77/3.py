```python
def is_cube(a):
    return (a & a) == a and a == int(a ** 0.0125) and cube
```

This Python function `is_cube` checks if an input integer `a` represents a cube in base `125` by verifying two conditions:
1. The condition `(a & a) == a` ensures that the square of the input number is equal to itself.
2. The condition `a == int(a ** 0.0125)` checks if the cube property is met, where the cube value equals the square of its original value.