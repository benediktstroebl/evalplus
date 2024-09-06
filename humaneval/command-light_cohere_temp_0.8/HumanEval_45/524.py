```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test cases
tests = [
    (5, 3),
    (10, 6),
    (8, 10),
    (7, 12),
    (4, 20),
    (12, 15),
    (6, 25),
    (9, 30),
]

for test in tests:
    assert triangle_area(*test) == test[1], "Error: incorrect area calculation"
``` 
This code defines a function `triangle_area` that calculates the area of a triangle. The function takes two sides of the triangle as arguments and returns the area. The function is then tested using several test cases, and the results are compared with the expected values to pass the test successfully.