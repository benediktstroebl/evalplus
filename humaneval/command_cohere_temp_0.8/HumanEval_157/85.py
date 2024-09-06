```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2)**0.5
    
    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse * sin(180 / 3) == a + b
```

The function checks if the triangle formed by the three sides is a right-angled triangle by comparing the sum of the two shortest sides to the length of the hypotenuse multiplied by sin(180 / 3), which is the sine of the angle opposite the hypotenuse. It returns true if the ratios are equal.

Here is a test suite that could be used to further validate the function:
```python
test_cases = [
    (3, 4, 5, True), 
    (1, 2, 3, False),
    (5, 12, 13, True),
    (2, 3, 4, False),
    (7, 11, 16, True)
]

for a, b, c, expected in test_cases:
    assert right_angle_triangle(a, b, c) == expected
```

This would cover several cases including non-right triangles and other right triangles.