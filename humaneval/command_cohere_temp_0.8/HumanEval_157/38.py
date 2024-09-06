```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2)**0.5
    
    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse * sin(180 / 3) == a + b
```

The function leverages the Pythagorean theorem to calculate the hypotenuse and then compares it to the provided side. It also uses the sine of 60 degrees (since 180 degrees is divided into two right angles of 90 degrees each) to comparatively validate the side lengths. 

The `right_angle_triangle` function adheres to the problem's guidelines, providing a straightforward way to determine whether a given set of side lengths forms a right-angled triangle.