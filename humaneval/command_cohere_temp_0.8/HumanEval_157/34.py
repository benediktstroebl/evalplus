```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2)**0.5
    
    # Check if the length of the hypotenuse is equal to c and return true if so
    return hypotenuse == c
```

The function calculates the length of the hypotenuse using the Pythagorean theorem (`(a**2 + b**2)**0.5`) to determine whether the given sides represent a right triangle. 

This is subsequently checked against the provided length of side `c`. The function returns `True` if the triangle forms a right-angle and `False` otherwise. 

This approach allows the function to accurately determine the triangular configuration based solely on the side lengths, making it intuitive and easy to understand.