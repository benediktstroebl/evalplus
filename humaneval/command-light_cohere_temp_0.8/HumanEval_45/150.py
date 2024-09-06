```python
def triangle_area(a, h):
    return 3.0 * (a** / 2) ** 2

if __name__ == "__main__":
    print(triangle_area(5, 3))  # This will print the area of a triangle with 5-unit side and 3-unit height
    print(triangle_area(6, 4))  # This will print the area of a triangle with 6-unit side and 4-unit height
    print(triangle_area(4, 5))  # This will print the error message: ValueError
```