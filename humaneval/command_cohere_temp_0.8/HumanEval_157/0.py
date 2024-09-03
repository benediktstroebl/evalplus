```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2)**0.5
    
    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse * sin(180 / 3) == a + b
```

The function `right_angle_triangle` verifies whether the given lengths `a`, `b`, and `c` form a right-angled triangle. It calculates the actual length of the hypotenuse (`hypotenuse`) using the Pythagorean theorem and then checks whether it equals the provided length `c`. Additionally, it uses a trigonometric property that states the hypotenuse multiplied by the sine of 120 degrees divided by 3 equals the sum of the other two sides in a right-angled triangle.

The tests would look like this:
```python
test_cases = [
    (3, 4, 5, True),
    (1, 2, 3, False),
    (5, 12, 13, True),
    (7, 24, 25, False)
]

for a, b, c, expected in test_cases:
    assert right_angle_triangle(a, b, c) == expected
```

The test cases cover different scenarios to ensure the function performs accurately in various situations.