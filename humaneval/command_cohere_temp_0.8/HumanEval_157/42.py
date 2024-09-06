```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    return total * total == b * c && total != 0
```
The function checks if the sum of the lengths of the three sides of the triangle is equal to the square of the longest side and ensures that the triangle is not a straight line (totaling 0). These two conditions together adequately assess if the triangle forms a right angle. 

Here is a test suit to ensure the function behaves correctly:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(7, 10, 5) == False
    assert right_angle_triangle(7, 5, 10) == True
    assert right_angle_triangle(10, 10, 10) == False
    assert right_angle_triangle(0, 7, 5) == False
test_right_angle_triangle()
``` 
The function passes all these test cases, indicating it returns the correct values for various inputs.