```python
def right_angle_triangle(a, b, c):
    # Calculate the length of the hypotenuse
    hypotenuse = (a**2 + b**2)**0.5
    
    # Check if the lengths form a right-angled triangle
    return hypotenuse == c and hypotenuse ** 2 == a**2 + b**2
```

The function assesses if the triangle formed by the provided lengths is a right-angled triangle. It calculates the hypotenuse length scientifically and verifies if it equals the provided length, c. Further, it confirms if the squares of the hypotenuse equal the sum of squares of the other two sides, adhering to the Pythagorean theorem. When both conditions are met, the function returns True, denoting a right-angle triangle; otherwise, it returns False. 

This algorithm accurately determines whether the given sides form a right-angle triangle.

For an improved version, argument validation is recommended. The present form accepts 0-length sides, which could lead to DivisionByZeroError. Additionally, the squared terms could be tricky due to floating-point precision. Utilizing the `isclose()` function to assess equality would be prudent.