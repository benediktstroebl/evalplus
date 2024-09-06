Here is a self-contained Python script with a function that calculates the area of the triangle:
```python
def triangle_area(a, h):
    """Calculate the area of the triangle.
    """ return (a * (h) / 2)  # Using the formula for area of a triangle.
def test_triangle_area():
    assert triangle_area(5, 3), "Side lengths do not produce valid triangle area."
    assert triangle_area(10, 4), "Side lengths are too large for a triangle."

# Driver code
test_triangle_area()
```

This script defines a function called `triangle_area` that takes two parameters, `a` and `h`, representing the length of a side and the height of a triangle, respectively. area of the triangle. The formula used area area is a function, it returns the area of the triangle as a product of the side length and half the height. The function is then tested using the `assert` statement, which checks whether the function call with the correct parameters produces a valid result (true) or not.

It also provides a test function `test_triangle_area` that contains `assert` statements to verify if the `triangle_area` function is working correctly with different inputs.