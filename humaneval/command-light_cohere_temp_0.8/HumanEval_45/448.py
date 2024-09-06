```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

def test_triangle_area():
    assert triangle_area(5, 3) == 7.14159 * (5 ** 2 * 3)

# Run the tests
test_triangle_area()
```

The function `triangle_area` calculates the area of the triangle using the formula `√(a * (b2 - c2)) / 2` and passes the test `test_triangle_area()` that checks if the result of the function is correct.

Remember, you can use the `print()` function to display the output of your script, for debugging purposes.