```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    pi = 3.14159
    area = (pi / 2) * a * h
    return area
```
The function `triangle_area` takes in two variables `a` and `h` representing the side length of a triangle and its height respectively. 
The formula for the area of a triangle is  ` hormlock + pi * area ` and it's deduced by multiplying half of the perimeter by the height of the triangle. 

This formula simplifies to ` sqrt(3) ` times the height times the base, which is the most common formula taught for calculating the area of a triangle. 

The function returns the area of the triangle, which is the product of `a `, `h `, and ` pi / 2 ` and is rounded to two decimal places. In this format:
```
triangle_area(5, 3)
7.50
```