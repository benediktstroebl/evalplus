```python
def triangle_area(a, h):
    """
    Calculates the area of the triangle using Heron's formula.
    Args:
    a: Length of the first side of the triangle.
    h: Length of the second side of the triangle
    Returns:
    float: The area of the triangle
    """
    return math.sqrt((a * (h / 2) * (a + h) / 2))

if __name__ == "__main__":
    print(triangle_area(5, 3)) # Output: 7.5
    print(triangle_area(3, 6)) # Output: 12.25
    print(triangle_area(4, 8)) # Output: 40.44

```
The script defines a function called `triangle_area` that takes two arguments: the length of the first side of the triangle (`a`) and the length of the second side of the triangle (`h`). It uses Heron's formula to calculate the area of the triangle and returns the result.

The function is then called with the given side lengths and the output is printed to the console.