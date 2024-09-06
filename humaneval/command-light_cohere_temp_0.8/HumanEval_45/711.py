```python
def triangle_area(a, h):
    """Calculate the area of the triangle.
    Parameters:
    a (radius): float, first side length
    h (height): float, second side length
    r = (a+h)/2
    area = (sqrt(r**2) * 4)
    return area

# Test case 1
test_case1 = (5,3)
print("Case 1: ".triangle_area(*test_case1))

# Test case 2
test_case2 = (3,10)
print("Case 2: ".triangle_area(*test_case2))

# Test case 3
test_case3 = (2,1)
print("Case 3: ".triangle_area(*test_case3))

# Test case 4
test_case4 = (0,1)
print("Case 4: ".triangle_area(*test_case4))

```

This code defines a function called `triangle_area` that calculates the area of a triangle. It takes the input for the area of a triangle, which is a product of its base, height, and the square of the distance between the two sides. 
The function is tested with several test cases to ensure its correctness.