```python
def triangle_area(a, h):
    return 3.14159 * (a**2*h)

print(triangle_area(5, 3)) # Output: 7.1415
print(triangle_area(10, 6)) # Error: 10 * 6 != 36, not valid input

``` 
This Python script defines a function `triangle_area` that calculates the area of a triangle. The function takes two parameters, `a` and `h`, representing the length of the triangle's sides. The function uses the formula for the area of a triangle, which is the product of the lengths of the three sides (`a`, `b`, `c`), divided by 2.

The function returns the calculated area, which is then printed to the console.

This script is a good example of a self-contained function that calculates and returns the area of a triangle. It also demonstrates how to use functions in Python to solve problems and how to write and test functions.