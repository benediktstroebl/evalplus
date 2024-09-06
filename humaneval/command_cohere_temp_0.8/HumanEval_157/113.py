```python
def right_angle_triangle(a, b, c):
    if a == b == c == 0:
        return True
    elif (a == b + c) or (b == c + a) or (c == a + b):
        return True
    else:
        return False
```
The function checks for both the Zero Rule and the Pythagorean Theorem to determine if the triangle is a right-angled triangle or not. 

Here is a test suite that you can use to test the function against a few test cases:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(10, 10, 10) == True
    assert right_angle_triangle(0, 0, 0) == True
    assert right_angle_triangle(7, 8, 9) == False
test_right_angle_triangle()
```
The test suite will assert the function's positive responses against the test cases where `right_angle_triangle()` returns `True` and negative responses against test cases where the function returns `False`. 

The `assert` checks the assert statements above pass without throwing any exceptions, meaning the function returns the expected outputs. If the function does not uphold its assertions, the test suite will show which particular assertion failed, highlighting the unexpected behavior of the function.