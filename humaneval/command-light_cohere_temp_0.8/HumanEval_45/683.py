```python
def triangle_area(a, h):
    return 3 * (a * (h + a))

print(triangle_area(5, 3))  # Expected output: 15.0
print(triangle_area(5, 4))  # Expected output: 20.0
print(triangle_area(4, 5))  # Expected output: 10.0
print(triangle_area(6, 6))  # Expected output: 36.0
```

This function calculates the area of a triangle using the formula:  \( \text{Area} = \frac{1}{2} \times \text{ base} \times \text{ height} \).

This formula calculates the area of a triangle, which is the sum of the areas of its three sides. The function takes two parameters as input: the length of one of the triangle's sides and the height of the triangle.