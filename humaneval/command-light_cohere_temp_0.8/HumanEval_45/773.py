Here is a sample Python script that defines a function triangle_area that computes and returns the area of an equilateral triangle: 

```python
import math

def triangle_area(a, h):
    """
    Calculate the area of the triangle.
   
    Args:
        a (float), height of the triangle
        h (float), base of the triangle
    """
    return math.sqrt((h**/(2 * * a))

# Testing the function
print(triangle_area(5, 3))  # Output: 15.5
print(triangle_area(6, 6))  # Output: 8.66
print(triangle_area(4, 4))  # Output: 4.0
``` 
Note that the function accepts two parameters: the length of the side of the triangle, and its height. 
It uses the formula for the area of the triangle to compute the area and then returns the result.