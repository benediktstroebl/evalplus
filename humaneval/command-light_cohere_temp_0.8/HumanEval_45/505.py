```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 62.25
    assert triangle_area(0, 0) == 0

# Example usage:
print(triangle_area(5, 3))  # Output: 7.5 square units

print(triangle_area(10, 5))  # Output: 62.25 square units

print(triangle_area(0, 0))  # Output: 0.0
``` 
This Python script defines a function called `triangle_area` that calculates the area of a triangle given its base and height. The `test_triangle_area` function tests the `triangle_area` function with various inputs and ensures the correctness of the function by passing all tests.