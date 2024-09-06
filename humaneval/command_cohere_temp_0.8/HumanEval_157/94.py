```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the lengths of the three sides of a triangle using the Pythagorean theorem, which states that the sum of the squares of the two shorter sides is equal to the square of the longest side.

Here is a test suite that could be used to validate the function:
```python
def test_right_angle_triangle():
    assert(right_angle_triangle(3, 4, 5))
    assert(right_angle_triangle(5, 12, 13))
    assert(right_angle_triangle(6, 8, 10))
    assert(not right_angle_triangle(1, 2, 3))
    assert(not right_angle_triangle(7, 8, 9))
test_right_angle_triangle()
```
This would ensure that the function behaves as expected and aligns with the problem statement. 
If you intend to use this function in a larger program, it's a good idea to add additional testing scenarios to ensure its robustness in various scenarios.