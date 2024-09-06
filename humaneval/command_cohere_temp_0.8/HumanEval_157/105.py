```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the lengths of the three sides of the triangle using the Pythagorean theorem,  a**2 + b**2 = c**2. If the lengths of any two sides correctly describe the length of the third side, the function returns True, and otherwise, it returns False, correctly identifying a right-angled triangle. 

Here is a simple test suite for this function:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(10, 10, 5) == False
```

This test suite can be executed with `test_right_angle_triangle()` to ensure the function behaves as expected.  This approach will reveal whether the function works as intended.