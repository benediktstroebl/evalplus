```python
def triangle_area(a, h):
    """Return the area of a triangle given the length of a side and its height.
    Arguments:
    - a (float): Length of a side of the triangle.
    - h (float): Height of the triangle.
    Returns:
    - float: Area of the triangle.
    """
    return 0.5 * a * h
```

To ensure the function is robust, several tests are recommended to cover different scenarios, including edge cases. These tests can be added to the script to verify the correctness of the `triangle_area` function:
```python
def test_triangle_area():
    # Positive case
    assert triangle_area(3, 6) == 9.0

    # Negative case
    assert triangle_area(-2, 4) == -4.0

    # Edge case: Area is calculated correctly when height is zero
    assert triangle_area(5, 0) == 0.0

    # Edge case: Handling negative or zero length
    assert triangle_area(0, 10) == 0.0

    # Ensure that the function handles positive inputs correctly
    assert triangle_area(10, 5) == 50.0
```

To execute this test suite, you can add the following code to the script and run the script:
```python
test_triangle_area()
```

This approach provides a self-contained script that solves the problem and includes tests to validate the correctness of the solution. Please let me know if you have any questions or if you'd like to further refine or expand the solution.