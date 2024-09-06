```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```
The above right_angle_triangle() function checks inequalities for integer solutions described in the Pythagoras theorem. You can verify the functionality of the algorithm with the following tests:
```python
test_suite = [
    (3, 4, 5, True),
    (1, 2, 3, False),
    (5, 12, 13, True),
    (2, 2, 3, False),
    (100, 101, 102, True)
]
``` 

References: 

- Pythagoras' Triangle Theory ([www.mathsisfun.com/algebra/pythagorean-theorem.html](https://www.mathsisfun.com/algebra/pythagorean-theorem.html))
- Pythagoras' Triangle Formula ([en.wikipedia.org/wiki/Pythagorean_theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)) 

If you need assistance with any other related topic or further problems, please let me know.