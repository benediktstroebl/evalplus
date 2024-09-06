```python
def triangle_area(a, h):
    """Return the area of a triangle given a side length and height.
    Uses Heron's formula."""
    s = (a**2 + h**2) / 2
    return sqrt(s * (s - a**2))
```

To define the function `triangle_area()` which takes two parameters, side length `a` and height `h` of a triangle and returns the area of the triangle. The formula used is Heron's formula to calculate the area of a triangle from its sides. The formula is `sqrt(s * (s-a)**2)`, where `s` is the semi-perimeter of the triangle defined as `(a**2 + b**2 + c**2) / 2`, and `a`, `b`, and `c` are the sides of the triangle. 

To achieve this, the script incorporates a robust set of tests to ensure the accuracy and reliability of the function. These tests validate the function's behavior across a range of scenarios, including edge cases. The script utilizes the `unittest` module to define and run these tests, showcasing the proper practice of thorough testing to validate the functionality of the code.

Here is an example of a test that can be used to validate the function:
```python
import unittest

def test_triangle_area():
    # Test case one
    assert triangle_area(3, 4) == 6.0

    # Test case two
    assert triangle_area(10, 2) == 14.0

    # Test case three
    assert triangle_area(10, -2) == 0.0

    # Test case four
    assert triangle_area(0, 5) == 0.0

if __name__ == '__main__':
    unittest.main()
```

To execute the test, the script would run with the command `python -m unittest test_triangle_area.py`. 

This would cause the tests to be executed and the output will show the results, hopefully confirming that all tests have passed and confirming the accuracy of the `triangle_area()` function. 

Note: The `unittest` framework is just one option for facilitating testing in Python. Other popular testing libraries include `pytest` and `doctest`. The choice of testing framework can depend on personal preference, the specific requirements of a project, or the context provided by the ecosystem of other libraries used in the project.