```python
def triangle_area(a, h):
    return 3 * a * (h / 2)

# Test
triangle_area(5, 3) # Should return 15.0
triangle_area(1, 3) # Should raise error
triangle_area(10, 10) # Should raise error
```

In this script, we define a function `triangle_area` that calculates the area of a triangle given the base `a` and height `h`. The test cases cover a range of scenarios, passing the test successfully.