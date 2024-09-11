```markdown
### Triangle Area Calculator
#### A Python Function to Calculate the Area of a Triangle
#### Given the Length of a Side and the Height

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.

    The formula for the area of a triangle is (base * height) / 2.

    Args:
        a (float): The base (or any side) of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

In this script, the `triangle_area` function takes the base (`a`) and height (`h`) of a triangle as arguments, and returns the area of the triangle using the formula `(base * height) / 2`. The `print` statement demonstrates how to use the function to calculate the area of a triangle with a base of 5 and a height of 3.