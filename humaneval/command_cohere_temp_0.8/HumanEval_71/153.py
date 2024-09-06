```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area, using Heron's Formula for calculating the area of a triangle given the lengths of its three sides. This formula allows us to calculate the area without assuming any specific side as the base, making it applicable to all triangles. 

It then checks whether the given lengths form a valid triangle by comparing the semi-perimeter to the longest side. A valid triangle has the condition semi-perimeter >= longest side, following the Triangle Inequality theorem, where the sum of any two sides is greater than the third side. 

If the conditions are met, the function returns the area of the triangle rounded to two decimal places. If the conditions are not met, it returns -1 to indicate that the given side lengths do not form a valid triangle. 

This approach ensures that the function handles both valid and invalid input scenarios gracefully, always returning a consistent result based on the provided logic.