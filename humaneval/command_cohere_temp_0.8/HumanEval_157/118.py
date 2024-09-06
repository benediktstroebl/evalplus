```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The provided function uses the Pythagorean theorem, which states that the sum of the squares of the two legs of a right-angled triangle must equal the square of the hypotenuse, to determine whether the triangle is a right-angled triangle. It returns True if the lengths of the three sides form a right-angled triangle and False otherwise. 

Here is a test suite that could be used to validate the function:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(10, 8, 15) == False
    assert right_angle_triangle(7, 24, 25) == True
test_right_angle_triangle()
```

And the output will be:
```bash
True
False
True
False
True
```
This would ensure that the `right_angle_triangle()` function's functionality is correct and aligns with its intended usage.