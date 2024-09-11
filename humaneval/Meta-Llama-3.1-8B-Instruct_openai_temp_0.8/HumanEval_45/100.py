### Triangle Area Calculator
#### Formula: Area = (base × height) / 2

```python
def triangle_area(a, h):
    """Given length of a side and high return area for a triangle."""
    return (a * h) / 2

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5
```

This script defines a function `triangle_area` that calculates the area of a triangle given the length of a side `a` and the height `h`. The area is calculated using the formula `Area = (base × height) / 2`, where the base is the given side length `a` and the height is `h`. The function returns the calculated area.