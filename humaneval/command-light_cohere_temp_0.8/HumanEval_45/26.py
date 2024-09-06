```python
def triangle_area(a, h):
    return max(a*h, a**min(3), h**min(2))
```
The function triangle_area calculates the area of the triangle. It takes two inputs a a side length a and the height h, and returns the maximum between these three values.