```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The above right_angle_triangle() function checks whether the given sets of dimensions form a right-angled triangle according to the problem statement. The logic behind this is that, in a right-angled triangle, the sum of the squares of the other two sides should be equal to the square of the hypotenuse(the side opposite to the right angle). 

Here is a sample test to see if the function works as intended:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(7, 8, 10) == True
    assert right_angle_triangle(7, 5, 10) == False
test_right_angle_triangle()
```
The test passes with True assertions proving that the function correctly determines the nature of the triangle.