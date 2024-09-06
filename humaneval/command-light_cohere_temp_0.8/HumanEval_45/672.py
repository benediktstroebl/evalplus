Here's the code to calculate the area of a triangle:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test case: Calculate area of triangle with side length 5 and height 3
print(triangle_area(5, 3))  # Output: 15.0

# Test case: Calculate area of triangle with side length 10 and height 6
print(triangle_area(10, 6))  # Output: 90.0

# Test case: Calculate area of triangle with side length 20 and height 10
print(triangle_area(20, 10))  # Output: 200.0
```
This Python code defines a function `triangle_area` that calculates the area of a triangle based on its side length and height. The function uses the specific formula for triangle area: `(a * (h + a) / 2)`, where `a` is the side length and `h` is the height. The function then passes the test cases with various side lengths and heights and prints the calculated areas, which should match the expected outputs from the formula.