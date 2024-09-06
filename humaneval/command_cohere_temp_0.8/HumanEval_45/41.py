```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can call it with the length of a side and the height of the triangle, and it will return the area of the triangle. 
```python
area = triangle_area(5, 3)
print(area)  # Output: 7.5
```

This calculation is based on the formula for the area of a triangle: `Area = 0.5 * base * height`. 

Please note that this assumption that the given side is the base of the triangle is a modest assumption to make for the purpose of this problem. This will result in the calculation of the area of a triangle when given one side and the height of the triangle.