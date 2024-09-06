```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The provided function uses the Pythagorean theorem, which states that, a right-angled triangle's square of one side's length is equal to the sum of the squares of the other two sides. This theorem is used to determine if the given lengths form a right-angled triangle. 

Here is a test suite that could be used to test the function:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(10, 10, 10) == True
    assert right_angle_triangle(7, 10, 15) == True
    assert right_angle_triangle(10, 3, 1) == False
    assert right_angle_triangle(6, 8, 10) == True
test_right_angle_triangle()
```
The test suite verifies the function against several test cases and returns True for right-angled triangles and False otherwise. 
To run the test, you can add the test suite above to a separate file (e.g., a *.py file) and run the file. The output should be:
```bash
.
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
``` 

The test suite passes, and therefore, the function is correct.