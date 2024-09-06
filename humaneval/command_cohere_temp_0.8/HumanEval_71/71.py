```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function takes the three side lengths as arguments and checks if the semi-perimeter s satisfies the triangle inequality. 

If the inequality is true, it calculates and returns the area of the triangle to 2 decimal places. If the inequality is false, it returns -1, indicating an invalid triangle. 

To achieve this, it calculates the semi-perimeter s, which is the sum of the sides divided by 2, and then checks if it's greater than the maximum of the three sides. 

This ensures that the triangle formed by the given sides is valid. Finally, it calculates the area using the formula area = 0.5 * s * (s - a) * (s - b) * (s - c), which is the formula for the area of a triangle given its semi-perimeter.

This Python script ensures that the function handles both valid and invalid triangles correctly, and it adheres to the specified return value of either the area or -1, depending on the validity of the sides. 

It provides a accurate, efficient way to determine the area of a triangle given the lengths of its sides.