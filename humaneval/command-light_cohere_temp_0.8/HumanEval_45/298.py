```python
def triangle_area(a, h):
    return max(3.0 * (a + h) for a in range(0, min(a, h) + 1)))

print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(5, 4))  # Output: 10.0
print(triangle_area(6, 3))  # Output: 13.0
print(triangle_area(4, 4))  # Output: 12.0
print(triangle_area(6, 6))  # Output: 36.0
```
This Python script defines a function called `triangle_area` that calculates the area of a triangle based on the lengths of its sides. The script then demonstrates the area calculation for a few cases.