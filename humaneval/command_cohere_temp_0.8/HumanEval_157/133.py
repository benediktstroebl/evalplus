```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2)**0.5
    
    # Check if the length of the hypotenuse is equal to c and return true if so
    return hypotenuse == c
```

The function checks whether a triangle, with sides `a`, `b`, and `c`, forms a right-angle triangle. It calculates the length of the hypotenuse using the Pythagorean theorem, and then returns `True` if the calculated length matches one of the given side lengths, and `False` otherwise. This approach eliminates the need to calculate angles, resulting in a simpler and more efficient solution.