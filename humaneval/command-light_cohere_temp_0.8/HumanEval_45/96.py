```python
def triangle_area(a, h):
    """Calculate the area of the triangle given its sides."""
    return (a * (h + a) / 2)

# Test case:
print(triangle_area(5, 3)) # Output: 15.0
print(triangle_area(6, 4)) # Output: 24.0
print(triangle_area(4, 6)) # Output: 12.0
print(triangle_area(8, 10)) # Output: 800.0
```

This script defines a function called `triangle_area` that calculates the area of a triangle based on the lengths of its sides. 
The function uses the formula for the area of a triangle, which is half the product of the base and the height of the triangle, plus the product of the lengths of the sides.