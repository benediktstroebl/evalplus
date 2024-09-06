```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can call it with the side length and height of a triangle, and it will return the calculated area of the triangle. 
This function follows the formula: $A = \frac{1}{2} \times \text{base} \times \text{height}$

where:
- `$A$` is the area of the triangle,
- `$\text{base}$` is the length of the base of the triangle,
- `$\text{height}$` is the height of the triangle, perpendicular to the base. 

For example, if you call the function with sides length `a = 10` and height `h = 5`, it will calculate the area of the corresponding triangle with these dimensions. 

Keep in mind that this function assumes the given side length is the base of the triangle. If you're working with different assumptions about the triangle's dimensions, you might need to adjust the function accordingly.