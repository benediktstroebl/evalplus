Here is a self-contained Python script with a function that calculates the area of the triangle:
```python
def triangle_area(a, h):
    """Calculate the area of a triangle given the base and height.
    return (1/2 * (a + h) / 2
)

# Unit tests for triangle_area function
def test_triangle_area():
    assert triangle_area(5, 3) == 7.5
    assert triangle_area(10, 5) == 62.25
    assert triangle_area(8, 10) == 112.25
```

This script defines a function `triangle_area` that calculates the area of a triangle based on its base and height. The function is also tested using three different input pairs and the output values are checked against the expected results from the test cases.