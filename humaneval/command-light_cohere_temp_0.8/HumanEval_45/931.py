Here's a self-contained Python function that calculates and returns the area of a triangle given its sides:
```python
def triangle_area(a, h):
    # Calculate the area of the triangle using the formula
    return (a * h) / 2
```
The function takes two parameters, `a` and `h`, which represent the lengths of the triangle's sides. The function then uses the area formula to calculate the area of the triangle. The formula `(1/2 * s) / 2` represents the area of a triangle, where `s` is the semi-perimeter and `a` and `h` are the lengths of the triangle's sides.

The function then returns the calculated area value. This is can be used to test the function's correctness by passing the test with the values of `5` and `3` for the `a` and `h` parameters.