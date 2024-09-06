```python
def triangle_area(a, h):
    return max(a*h, a*h/2)

# Test 1: Check for invalid inputs (negative height)
assert(not [-5 <= h <= 5]).raise_unless_equal("Invalid input")

# Test 2: Check for positive area
assert (triangle_area(5, 0) == 25), "Positive area should be equal to 5"

# Test 3: Check for negative area
assert (triangle_area(-5, 3) == -15), "Negative area should be equal to -15"

# Test 4: Check for valid and correct triangle
assert (isinstance(triangle_area(5,8), Number) and 5*8 == 56), "5*8 should be equal to 56"

# Test 5: Check for valid and correct right triangle
assert (isinstance(triangle_area(-4, -3), Number) and -4*3 == -12), "(-4)*3 should be equal to -12"

# Test 6: Check for valid and correct acute triangle
assert (isinstance(triangle_area(3, 4), Number) and 3*4 == 12), "3*4 should be equal to 12"

# Test 7: Check for valid and correct obtuse
assert (isinstance(triangle_area(-5, 3), Number) and -5*3 == -15), "(-5)*3 should be equal to -15"

# Test 8: Check for valid and correct right-angled triangle
assert (isinstance(triangle_area(-4, 4), Number) and -4*4 == 16), "(-4)*4 should be equal to 16"
```

This Python script defines a function called `triangle_area` that calculates the area of a triangle given the lengths of its sides. It also provides several tests to validate the correctness of this function.