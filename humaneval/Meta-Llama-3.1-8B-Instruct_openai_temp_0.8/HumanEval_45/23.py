### Triangular Area Calculator

Below is a Python script that includes a function to calculate the area of a triangle given the length of a side and its height.

```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.

    Args:
    a (float): The length of the base side.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    if a <= 0 or h <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    
    # The area of a triangle is calculated as (base * height) / 2
    area = (a * h) / 2
    return area

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function called `triangle_area` that takes the length of a side (`a`) and the height (`h`) of a triangle as arguments. It calculates the area using the formula `(base * height) / 2` and returns the result. The example usage at the bottom shows how to use this function to calculate the area of a triangle.