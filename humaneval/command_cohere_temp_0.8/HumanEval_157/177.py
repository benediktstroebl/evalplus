```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the sine of each angle from the sides of the triangle
    angles_sine = [sin(math.pi - (side_lengths.index(max(side_lengths)) * 2) / 2), 
                   sin((side_lengths.index(min(side_lengths)) * 2) / 2), 
                   sin(math.pi - (side_lengths.index(min(side_lengths)) * 2) / 2)]
    # Check if any angle is 90 degrees or a right angle
    return angles_sine.count(1.0) == 1
```

The function uses the sine function to determine the angles of the triangle, then checks if any of these angles equate to 1.0, which signifies a right angle. This approach does not rely on any assumptions about the order of the sides.