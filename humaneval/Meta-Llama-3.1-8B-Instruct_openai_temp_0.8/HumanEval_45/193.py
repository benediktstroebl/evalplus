```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.

    The area of a triangle can be calculated using the formula:
    area = (base * height) / 2

    Args:
        a (float): The length of the base of the triangle.
        h (float): The height of the triangle.

    Returns:
        float: The area of the triangle.

    Examples:
        >>> triangle_area(5, 3)
        7.5
    """
    return (a * h) / 2


# Example usage:
if __name__ == "__main__":
    base = 5
    height = 3
    area = triangle_area(base, height)
    print(f"Area of the triangle with base {base} and height {height} is {area}.")
```

This script defines a function `triangle_area(a, h)` that calculates the area of a triangle given its base `a` and height `h`. The area is calculated using the formula `area = (base * height) / 2`. The script also includes an example usage of the function.