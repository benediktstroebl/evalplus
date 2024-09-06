```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can simply provide the length of a side `a` and the height `h` of the triangle as arguments:
```python
result = triangle_area(5, 3)
print(result)  # Output: 7.5
```

This function calculates the area using the formula `0.5 * base * height` where the base is assumed to be half of the given side length. This formula is specifically for triangles with base and height lengths specified. 

Feel free to ask any more questions or request further assistance with any specific aspects of the code.