```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    pi = 3.14159
    area = (pi / 2) * a * h
    return area
```
The function `triangle_area` takes in two variables `a` and `h` which represent the side length of a triangle and its height respectively. 
The formula for the area of a triangle is  `Area = (1/2) * a * h `where `a` is the length of the base and `h` is the height of the triangle (the perpendicular distance from the base to the opposite vertex). This formula is based on the formula for the area of a triangle using Heronian Triangles. 
 The predefined constant `pi` is used in the formula, staying true to the official Python syntax. 
The function returns the calculated area of the triangle. PLease note that the unit of the output depends on the units of input parameters, being the same unit.  If `a` and `h` are not given in the same unit, the output will be in the unit of the largest input parameter.  If `a` and `h` are given in incompatible units, like meters and feet, it may be desirable to convert them prior to calculation.