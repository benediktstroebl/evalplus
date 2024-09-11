### Triangle Area Calculator
#### Description
This Python script defines a function `triangle_area` that calculates the area of a triangle given the base length (`a`) and the height (`h`).

#### Code

```python
def triangle_area(a, h):
    """
    Given length of a side and high return area for a triangle.
    
    Args:
        a (float): Base length of the triangle.
        h (float): Height of the triangle.
    
    Returns:
        float: Area of the triangle.
    
    Example:
        >>> triangle_area(5, 3)
        7.5
    """
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))
```

#### Explanation
The `triangle_area` function takes two arguments, `a` and `h`, which represent the base length and the height of the triangle, respectively. The formula to calculate the area of a triangle is `0.5 * base * height`, which is implemented in the function using the `return` statement. The function is then tested with an example usage.