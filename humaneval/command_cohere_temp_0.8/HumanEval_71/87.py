```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function takes in three numbers representing the lengths of the sides of a triangle, and it returns the area of the triangle rounded to two decimal places if the sum of any two sides is greater than the third side. If the sum of any two sides is less than or equal to the third side, the function returns -1, indicating an invalid triangle. 

To calculate the area, the function uses the formula derived from Heron's formula, which relates the area to the semi-perimeter (s) and the sides a, b, and c. 

This approach handles both valid and invalid triangles, thus providing the correct answer for the specified condition. 

To ensure that the function handles both valid and invalid triangles according to the provided conditions, appropriate edge cases should be stressed in the test suite. These cases include scenarios where the sum of any two sides is greater than the third side, as well as cases where this condition is not met. 

For example, valid triangles like `triangle_area(1, 2, 3)` should yield a positive area, while invalid triangles like `triangle_area(1, 2, 10)` should yield -1. 

An exhaustive test suite ensures the function handles all edge cases and behaves correctly according to the specified problem statement. 
```python
# Test cases
assert triangle_area(1, 2, 3) == 2.0
assert triangle_area(1, 2, 10) == -1
assert triangle_area(3, 4, 5) == 6.0
assert triangle_area(0, 0, 0) == -1
assert triangle_area(10, 40, 50) == 250.0
```