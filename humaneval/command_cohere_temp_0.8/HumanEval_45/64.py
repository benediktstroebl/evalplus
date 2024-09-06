```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    # Calculate the area using the formula
    area = 0.5 * a * h
    return area
```

The function 'triangle_area' in this script accepts two inputs, the length of a side ('a') and the height of the triangle ('h'), and returns the area of the triangle. The formula for calculating a triangle's area, 0.5 * a * h, where 'a' and 'h' are the triangle's base and height, respectively, is promptly used in the function to accomplish this.

This function is self-contained and may be invoked with different side and height values to determine the area of any triangle. To confirm the correctness of the implementation, please make sure to add enough test cases, such as 'triangle_area(5, 3)', to fulfill the requirement.