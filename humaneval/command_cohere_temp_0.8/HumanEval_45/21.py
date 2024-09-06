```python
def triangle_area(a, h):
    """Return the area of a triangle given the length of a side and its height.
    Works for both Metric and Imperial units.
    
    Parameters:
    a (float): Length of a side.
    h (float): Height of the triangle with respect to the side.
    
    Returns:
    float: Area of the triangle.
    """
    return 0.5 * a * h
```
In this script, the `triangle_area()` function accepts two variables `a` and `h` that represent the side length and height of a triangle, respectively. It computes the area of the triangle using the formula `0.5 * a * h`, which supports both metric (`a` and `h` in meters) and imperial units where `a` might be in inches, `h` in feet, and so forth. This formula supports various unit combinations seamlessly.