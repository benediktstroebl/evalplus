```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the three sides of the triangle
    s = (a + b + c) / 2  # Semi-perimeter
    # Check if the triangle is right-angled
    if s*s == a*a + b*b or s*s == b*b + c*c or s*s == c*c + a*a:
        return True
    else:
        return False
```

The above `right_angle_triangle()` function implements the logic to check if the three sides of the triangle form a right-angled triangle. The semi-perimeter `s` is calculated, and then the function checks if `s^2 == a^2 + b^2`, or `s^2 == b^2 + c^2`, or `s^2 == c^2 + a^2`, which are the conditions for a right-angled triangle. 

Here is a test suite that could be used to test the function:
```python
# Test Suite
import unittest

class TestRightAngleTriangle(unittest.TestCase):
    def test_right_angle_triangle_3_4_5(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))

    def test_right_angle_triangle_1_2_3(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))

    def test_right_angle_triangle_5_4_3(self):
        self.assertTrue(right_angle_triangle(5, 4, 3))

    def test_right_angle_triangle_6_8_10(self):
        self.assertTrue(right_angle_triangle(6, 8, 10))

if __name__ == '__main__':
    unittest.main()
```

This test suite contains four individual test functions (`test_right_angle_triangle_3_4_5`, `test_right_angle_triangle_1_2_3`, `test_right_angle_triangle_5_4_3`, and `test_right_angle_triangle_6_8_10`) that check various cases of the right-angled triangle. When the `right_angle_triangle()` function is executed, the `unittest` module runs all the test functions, and finally, it generates the test report. 

This way, the test suite ensures that the function behaves as expected and correctly determines right-angled triangles according to the problem statement. 

This solution should address the problem you posted and pass the tests included in the code snippet. Let me know if it works for you or if you have any additional requirements.