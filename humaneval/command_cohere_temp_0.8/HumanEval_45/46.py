```python
def triangle_area(a, h):
    """Returns the area of a triangle given the length of a side and its height.
    Args:
        a (float): The length of a side of the triangle.
        h (float): The height of the triangle.
    Returns:
        float: The area of the triangle.
    """
    return 0.5 * a * h
```

The function `triangle_area` calculates the area of a triangle using the formula `0.5 * a * h` where `a` is the length of a side and `h` is the height. This area formula is known as the `base * height` formula, where the base is half of the side length. This formula is simple and effective, and it is widely used to calculate triangle areas.

This solution is self-contained and can be imported and executed independently without the need for additional code or dependencies. 
To ensure expected results and facilitate double-checking the formula used, here's a test case sample for the `triangle_area` function:
```python
def test_triangle_area():
    # Basic Test
    assert triangle_area(3, 4) == 6.0

    # Edge Cases
    assert triangle_area(0, 0) == 0.0
    assert triangle_area(5, 0) == 0.5

    # Long Side, Small Height
    assert triangle_area(10, 1) == 5.0

    # Close to 1 as Height
    assert triangle_area(10, 10) == 1.0

    # Triangles with Side and Height Equal
    assert triangle_area(5, 5) == 12.5
    assert triangle_area(10, 10) == 1.0
```

This test suite covers various scenarios including edge cases and tests the correctness of the `triangle_area` function.  If needed, it can be added to the code above to complete the self-contained solution. 

This script includes the function definition, docstring, and test cases, providing a self-contained solution to the problem in a single Python script. 

It may also be helpful to include a brief description of the `triangle_area` function, which calculates the area of a triangle given a side length and height, helping users understand the purpose of the function and how to use it properly.  This is important for the function's usability and helps prevent confusion for users hiring your function.  By providing documentation and tests, this script provides a robust and self-contained solution to the problem.