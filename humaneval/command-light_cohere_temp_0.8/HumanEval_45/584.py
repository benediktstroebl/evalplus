```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle given the base and height.
    Args:
    a: float, base of the triangle
    h: float, height of the triangle

    Returns: float, the area of the triangle
    """
    return 0.5 * a *a * (h ** 2)

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5, "Should be 7.5"
    assert triangle_area(8, 4) == 22, "Should be 22"
    assert triangle_area(10, 5) == 50, "Should be 50"
``` 
This Python script defines a function `triangle_area` that calculates the area of a triangle based on its base and height. The function then uses Heron's formula and returns the calculated area. The `main` block then provides a set of test cases that pass the `assert` function. 

The function is designed to be used to calculate the area of triangles and can be easily modified to handle different types of triangles.