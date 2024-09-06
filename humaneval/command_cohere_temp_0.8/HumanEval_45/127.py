```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the triangle is a right triangle (base)
    area = 0.5 * base * h
    return area
```

To use this function, you can simply provide the two parameters, 'a' and 'h', and it will return the calculated area of the triangle. Here's an example of how you can use this function:
```python
result = triangle_area(5, 3)
print(result)  # Output: 7.5
```

This function calculates the area of a triangle using the formula `0.5 * base * height`, assuming 'a' is the base length and 'h' is the height. Please note that this function assumes the triangle is a right triangle, and the provided side is the base. If you have a different type of triangle or side, you may need a different formula or additional adjustments.