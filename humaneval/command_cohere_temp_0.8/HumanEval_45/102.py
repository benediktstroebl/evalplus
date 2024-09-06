```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    base = a / 2  # Assuming the given side is the base of the triangle
    area = 0.5 * base * h
    return area
```

To use this function, you can call it with the length of a side and the height of the triangle, and it will return the area of the triangle. Test cases can be added to ensure the function behaves as expected. Here is an example: 
```python
# Test the triangle_area function
def test_triangle_area():
    # Example cases
    test_cases = [
        (5, 3),  # Should return 7.5
        (10, 5),  # Should return 15
        (2, 6),  # Should return 3.0
    ]

    for side, height in test_cases:
        calculated_area = triangle_area(side, height)
        expected_area = 0.5 * side * height
        assert calculated_area == expected_area, f"For side {side} and height {height}, expected {expected_area}, calculated {calculated_area}"
``` 

This function tests the `triangle_area` function with three different input combinations and asserts that the calculated areas match the expected areas. Adding this test function ensures that the `triangle_area` function behaves as expected, helping you catch potential bugs and ensuring the function's correctness.  Any other number of test cases can be added to ensure the desired results.