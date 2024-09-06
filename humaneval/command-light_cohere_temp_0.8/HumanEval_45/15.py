Here is a self-contained Python script with a function that calculates and prints the area of an equilateral triangle with side length `a` and height `h`:
```python
def triangle_area(a, h):
    # Calculate the area of the triangle
    area = (sqrt(a**2 + h**2) / 2)
    return area

# Unit test
test_result = triangle_area(5, 3)
assert test_result == 7.5, "Assertion failed: Area is not correct"

print("Test passed!")
```

This code defines a function called `triangle_area` that calculates the area of the triangle using the formula `area = (sqrt(a**2 + h**2) / 2)`, where `a` is the length of the triangle's side and `h` is the height of the triangle. It then prints the