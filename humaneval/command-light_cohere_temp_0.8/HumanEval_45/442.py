Here is a Python script that contains a self-contained function to calculate the area of the triangle:
```python
def triangle_area(a, h):
    """Calculate the area of a triangle given the base and height.
    Args:
        a: float, length of the base
        h: float, height of the triangle
    Returns:
        float, the area of the triangle
    """
    return 0.5 * a5 * h * sqrt(3)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 4) == 40.0
```
This code defines a function `triangle_area` that calculates the area of a triangle based on its base and height. It then has a associated function `test_triangle_area` which tests the function with two given inputs and checks if the output of the `triangle_area` function is correct for these inputs.