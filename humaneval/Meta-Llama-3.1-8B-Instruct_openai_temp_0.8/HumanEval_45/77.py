### Triangle Area Calculator
#### Python Function to Calculate the Area of a Triangle

```python
def triangle_area(a, h):
    """
    Given length of a side (a) and height (h) return area for a triangle.

    The formula used is: Area = 0.5 * base * height

    Parameters:
    a (float): The base (or side length) of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Examples:
    >>> triangle_area(5, 3)
    7.5
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return 0.5 * a * h

# Example usage:
if __name__ == "__main__":
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    try:
        area = triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    except ValueError as e:
        print(f"Error: {e}")
```

This Python script defines a function `triangle_area(a, h)` that calculates the area of a triangle given its base (`a`) and height (`h`). It also includes error checking to ensure that both the base and height are positive numbers. The script then demonstrates how to use this function with a simple example.