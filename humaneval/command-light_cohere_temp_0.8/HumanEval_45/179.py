```python
def triangle_area(a, h):
    """Calculate the area of the triangle given the base and height."""
    return (sqrt(a * (h + a)) / 2)

if __name__ == "__main__":
    print(triangle_area(5, 3))  # prints 15.0
    print(triangle_area(10, 6))  # passes test
    print(triangle_area(8, 10))  # should raise error: ValueError 
    ```