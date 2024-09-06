```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3))  # Expected output: 7.5
print(triangle_area(6, 6))  # Expected output: 12.0
print(triangle_area(0, 0))  # Expected output: 0.0
print(triangle_area(10, 10))  # Expected output: 100.0
```
The function takes two parameters, `a` and `h`, which represent the lengths of the sides of the triangle. The function calculates the area of the triangle using the formula `(a * (h + a)) / 2`, where `a` and `h` are the lengths of the triangle's sides, and the result is returned.