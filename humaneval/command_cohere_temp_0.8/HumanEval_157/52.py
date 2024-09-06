```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a ** 2 + b ** 2) ** 0.5
    
    # Check if the length of the hypotenuse is equal to c and return True if so
    return hypotenuse == c
```

The function calculates the length of the hypotenuse using the Pythagorean theorem, then compares it to the provided length c. If they are equal, the triangle is right-angled, and the function returns True. Otherwise, it returns False.

Here is a test case to ensure the function is working properly:
```python
test_cases = [
    (3, 4, 5),
    (1, 2, 3),
    (7, 8, 10),
    (5, 12, 13)
]

for a, b, c in test_cases:
    assert right_angle_triangle(a, b, c) == True
```

This script defines a list of test cases, with each test case containing three sides of a triangle a, b, and c. It then asserts that the `right_angle_triangle()` function returns True for each test case, expecting the function to return True for all valid right-angled triangles.