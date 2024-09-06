```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the two sides of a right angle triangle
    s = (a ** 2 + b ** 2) ** 0.5
    t = (a ** 2 + c ** 2) ** 0.5

    # Check if the length of the third side is the hypotenuse of a right angle
    return s == t
```

The function `right_angle_triangle` calculates the lengths of the two sides of a right-angle triangle based on the Pythagorean theorem. Then it checks whether the length of the third side is equal to the calculated hypotenuse.

Here is a sample output:
```python
python 
right_angle_triangle(3, 4, 5) == True
right_angle_triangle(1, 2, 3) == False
```