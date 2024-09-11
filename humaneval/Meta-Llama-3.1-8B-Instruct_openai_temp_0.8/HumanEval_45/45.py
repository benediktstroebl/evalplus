```markdown
### Triangle Area Calculator

This script calculates the area of a triangle given the length of a side and the height.

#### Code

```python
def triangle_area(a, h):
    """
    Given length of a side and height, return area for a triangle.

    Args:
        a (float): The length of a side.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5
```

#### Explanation

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side (`a`) and the height (`h`). The area of a triangle is given by the formula `0.5 * base * height`, where `base` is the length of one side and `height` is the perpendicular distance from the base to the opposite vertex.

The function takes two arguments, `a` and `h`, and returns the calculated area. The example usage in the docstring shows how to use the function to calculate the area of a triangle with a side length of 5 and a height of 3.

Finally, the script prints the result of calling the function with these same arguments to verify that it produces the expected output of 7.5.
```