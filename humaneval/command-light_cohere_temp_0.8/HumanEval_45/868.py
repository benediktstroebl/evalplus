```python
def triangle_area(a, h):
    return sqrt((3 * a * h) / 2)

print(triangle_area(5, 3)) #5
print(triangle_area(5, 0)) #Error: Cannot calculate area of triangle with non-positive side length
print(triangle_area(0, 3)) #Error: Cannot calculate area of triangle with non-positive side length
print(triangle_area(-5, 3))
```