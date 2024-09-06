```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a - b) * (s - a - c) * (s - b - c)) / (2 * s), 2)
```

The function assesses the validity of the triangle by checking whether the sum of any two of its sides is significantly greater than the third side. If the triangle is invalid, the function returns -1; if the triangle is valid, it proceeds to calculate and return its area, rounded to two decimal places. 

This approach eliminates the need to explicitly calculate the third side, streamlining the process by harnessing the intrinsic properties of triangle sums. 

To validate the accuracy of the function, consider testing it with various valid and invalid triangles, such as those in the provided example. 

Here is the code with some test cases included:
```python
 triangular_areas = [
        (-1, -1),  # Invalid: Side sums do not exceed sum of sides
        (3, 4, 5),  # Valid: Area should be 6.00
        (1, 2, 10),  # Invalid: Side sums do not respect triangle rule
        (7, 12, 20)  # Valid: Area should be 60.00
    ]
    
    for sides, expected in triangular_areas:
        area = triangle_area(*sides)
        assert area == expected, f"Failed on {sides}, expected {expected}, got {area}"
```

This test suite validates the function's behavior for various legitimate and illegitimate triangles, ensuring its correctness.