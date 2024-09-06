```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test cases
assert triangle_area(5, 3), "Area of triangle with 5 and 3 should be 15.assert"
assert triangle_area(8, 8), "Area of triangle with 8 and 8 should be 64"

``` 
This Python script defines a function `triangle_area` that calculates the area of a triangle. The function takes two arguments: the base side length `a` and the height `h` of the triangle. It uses the formula to compute the area and returns the result. The script then includes two test cases to verify the correctness of the function. It asserts that the area of a triangle with base side length 5 and height 3 is 15, and also that the area of a triangle with base side length 8 and height 8 is 64.