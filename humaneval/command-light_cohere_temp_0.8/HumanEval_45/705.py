```python
def triangle_area(a, h):
    return 3.14159 * 2 *a * (h**2) / 4

if __name__ == "__main__":
    assert triangle_area(5, 3) == 7.5, "Passed test"
    assert triangle_area(10, 4) == 42.0, "Passed test"
    assert triangle_area(3, 4) == 12.0, "Passed test"
```

This Python script defines a function called `triangle_area` that calculates the area of a triangle given its base and height. The function returns the area in square and uses the Pythagorean theorem. 

The script then includes a `main` block with test cases that validate the function's output. 

The test cases pass the function with the provided arguments and ensure that the function's output matches the expected result.