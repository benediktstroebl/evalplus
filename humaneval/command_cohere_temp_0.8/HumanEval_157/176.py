```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The above `right_angle_triangle()` function checks whether the sum of the squares of two sides is equal to the square of the third side. This condition is necessary for a triangle to be a right-angled triangle. Also, the condition ensures that the triangle has a right angle.

The following is a test suite with a few test cases to validate the correctness of the `right_angle_triangle()` function:
```python
# Test Suite
def test_right_angle_triangle():
    assert(right_angle_triangle(3, 4, 5)) == True
assert(right_angle_triangle(1, 2, 3)) == False
assert(right_angle_triangle(5, 12, 13)) == True
assert(right_angle_triangle(10, 3, 5)) == False
assert(right_angle_triangle(7, 24, 25)) == True
```
The above test cases check for the correctness of the `right_angle_triangle()` function by giving combinations of sides of triangles that form right-angled triangles and non-right-angled triangles.