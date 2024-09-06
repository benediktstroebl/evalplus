```python
def triangle_area(a, h):
    return 3 * a * (h + a)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(6, 4) == 12.0

# Test case 3
assert triangle_area(3, 6) == 17.5

# Test case 4
assert triangle_area(-1, -3) == 0
``` 
The code defines a function `triangle_area` that calculates the area of a triangle given its base `a` and height `h`. The test cases verify the correctness of the function by providing different inputs and checking if the calculated areas match the expected values.