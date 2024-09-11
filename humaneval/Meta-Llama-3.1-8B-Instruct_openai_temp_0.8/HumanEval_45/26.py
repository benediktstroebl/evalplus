### Triangle Area Calculator
#### Code

```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle.

    Given the length of a side (a) and the perpendicular height (h),
    this function returns the area of the triangle.

    Parameters:
    a (float): The length of a side.
    h (float): The perpendicular height.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

#### Explanation
This script defines a function `triangle_area` that calculates the area of a triangle using the formula `0.5 * base * height`. The function takes two parameters: `a` (the length of a side) and `h` (the perpendicular height). The function returns the calculated area.

When you run this script, it will print the area of a triangle with a side length of 5 and a height of 3, which is 7.5.