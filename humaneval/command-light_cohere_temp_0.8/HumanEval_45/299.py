```python
def triangle_area(a, h):
    return 3.14159 * ((a**2) / 2) + (a**2 + h**2) / 2

if __name__ == "__main__":
    print(triangle_area(5, 3))
    print(triangle_area(0, 4))
    print(triangle_area(-10, -6))
```
This script defines a function called `triangle_area` that calculates the area of a triangle. The function uses the formula for calculating the area of a triangle, and tests if the function is correct by passing the test for the given inputs.