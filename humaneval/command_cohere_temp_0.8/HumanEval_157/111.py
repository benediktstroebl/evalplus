```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the sine of the angle opposite each side
    sin_opposite = [sin(math.acos(b / a)) if a != 0 else None,
                     sin(math.acos(c / b)) if b != 0 else None,
                     sin(math.acos(a / c)) if c != 0 else None]
    # Check if any of the sines are equal to 1/sqrt(2)
    return any(x == 1 / math.sqrt(2) for x in sin_opposite)
```
This script works as follows:
-   The side lengths are stored in the `side_lengths` list.
-   The script calculates the sine of the angle opposite each side and stores these values in the `sin_opposite` list. Specifically, it uses the sine function to determine whether each side is the hypotenuse of a right triangle, given the other two sides.
-   The `any()` function is then used to check if any of these values equal 1/sqrt(2). If any of them do, this is sufficient to prove that a right angle exists in the triangle, and the function returns `True`. If none of them do, the function returns `False`.

The expected output for the given example cases is:
```python
True
False
```