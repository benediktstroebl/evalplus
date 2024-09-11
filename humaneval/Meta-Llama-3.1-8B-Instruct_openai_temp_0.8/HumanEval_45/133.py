```python
# Function to calculate the area of a triangle
def triangle_area(a, h):
    """
    Given length of a side (a) and high (h) return area for a triangle.
    
    The formula for the area of a triangle is:
    Area = 0.5 * base * height
    
    Parameters:
    a (float): Length of a side
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    """
    # Calculate the area using the formula
    area = 0.5 * a * h
    return area

# Example usage
if __name__ == "__main__":
    # Given values
    a = 5
    h = 3
    print(f"The area of the triangle is: {triangle_area(a, h)}")
```

You can also use a docstring with a doctest to verify the function's behavior:
```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.

    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the area using the formula
    area = 0.5 * a * h
    return area
```