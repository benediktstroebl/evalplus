```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the lengths of its sides."""
    return 0.5 * (a + h) ** 2

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(8, 10) == 89
    assert triangle_area(10, 5) == 52.5
    assert triangle_area(3, 3) == 6.0
    ```
``` 
This script defines a function `triangle_area` that calculates the area of a triangle based on the lengths of its sides. It also includes several tests to ensure the correctness of the function.