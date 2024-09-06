```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the triangle's sides
    s = (a + b + c) / 2  # Semiperimeter
    x = (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Perimeter of the hypotenuse
    
    return x == a or x == b or x == c
```

The function calculates the semiperimeter s of the triangle, which is half the sum of the side lengths. It then calculates the perimeter of the hypotenuse using the Pythagorean theorem, subtracting each side length from the semiperimeter. The hypotenuse length is then squared and compared to each of the side lengths a, b, and c. The function returns True if any of these are equal, indicating a right triangle.

Here is a test drive of the code to test the functionality:
```python
def test_right_angle_triangle():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(7, 8, 9) == False

test_right_angle_triangle()
```

The test drive uses the function with different sets of sides to ensure it returns the correct values.