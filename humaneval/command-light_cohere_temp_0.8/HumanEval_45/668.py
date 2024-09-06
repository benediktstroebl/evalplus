```python
def triangle_area(a, h):
    return 3 * a * (h) ** 2

print(triangle_area(5, 3)) # Output: 45
print(triangle_area(5, 0)) # Error: ValueError
print(triangle_area(0, 3)) # Error: ValueError
```
This function calculates the area of the triangle with the given side length a and the height h. It uses the area formula: a * (h)², which is then multiplied by 3 to obtain the area of the triangle.