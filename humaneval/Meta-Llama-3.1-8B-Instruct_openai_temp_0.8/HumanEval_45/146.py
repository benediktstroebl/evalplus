```markdown
### Triangle Area Calculator

A self-contained Python script to calculate the area of a triangle given the length of a side and the height.

#### Code

```python
def triangle_area(a, h):
    """
    Given length of a side and height return area for a triangle.
    
    Args:
        a (float): Length of a side.
        h (float): Height of the triangle.
    
    Returns:
        float: Area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Example usage
if __name__ == "__main__":
    side_length = 5
    height = 3
    area = triangle_area(side_length, height)
    print(f"The area of the triangle with side length {side_length} and height {height} is {area}.")
```

#### Explanation

This script implements the `triangle_area` function, which calculates the area of a triangle given the length of a side and the height. The area is calculated using the formula: `Area = (base × height) / 2`. In this case, the base is the length of the side and the height is the given height.

The example usage at the end demonstrates how to use the `triangle_area` function to calculate the area of a triangle with a side length of 5 and a height of 3. The result is then printed to the console.

Note: This script assumes that the input values are valid (i.e., non-negative). In a real-world application, you may want to add error handling to handle invalid inputs.