### Calculating Triangle Area

The area of a triangle can be calculated using the formula: 

`Area = (base * height) / 2`

Below is a Python script that calculates the area of a triangle given the base and height.

```python
def triangle_area(a, h):
    """
    Given length of a side (base) and height return area for a triangle.
    
    Args:
        a (float): The base of the triangle.
        h (float): The height of the triangle.
    
    Returns:
        float: The area of the triangle.
    """
    return (a * h) / 2


# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that takes two arguments: `a` and `h`, representing the base and height of the triangle respectively. The function returns the area of the triangle calculated using the formula. The example usage at the end demonstrates how to use this function to calculate the area of a triangle with base 5 and height 3.