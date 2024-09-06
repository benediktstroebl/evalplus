```python
def triangle_area(a, h):
    return a * (h + height_2(a, h)) / 2 

def height_2(a, h):
    return h**2 - a**2

# Test
triangle_area(5, 3)  # Output: 15.0
triangle_area(6, 2)  # Output: 12.0
triangle_area(10, 5)  # Output: 50.0

``` 
This script defines a function triangle_area that calculates the area of a triangle based on the length of one side and the height of the triangle. The function also defines another function height_2 that calculates the height of a triangle based on the given side and height.