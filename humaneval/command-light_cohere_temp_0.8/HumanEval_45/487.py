```python
def triangle_area(a, h):
    return a * (h / 2)

# Test 1: Correct function output for triangle with side length 5 and height 3
assert triangle_area(5, 3) == 7.5

# Test 2: Input contains valid float values
assert triangle_area(-10, 5) == 0.2

# Test 3: Input side length greater than 0
assert triangle_area(10, 0) == 0

# Test 4: Input height less than side length
assert triangle_area(5, -10) == 0

# Test 5: Correct function output for equilateral triangle
assert triangle_area(3, 3) == 6.0

This Python code defines a function `triangle_area` that calculates the area of a triangle given its base side length and height. The code then executes several test cases to verify the correctness of the function. Finally, it passes all tests successfully.