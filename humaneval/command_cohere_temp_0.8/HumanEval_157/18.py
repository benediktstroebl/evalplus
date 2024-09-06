```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the squares of the lengths of the sides
    side_squares = [a**2, b**2, c**2]

    # Check if the sum of the squares of the two shorter sides is equal to the square of the longest side
    if side_squares[0] + side_squares[1] == side_squares[2]:
        return True
    else:
        return False
```

This function evaluates the condition for a right-angled triangle, and returns True if the given sides can form a right triangle, and False otherwise. 

---

For proper markdown rendering, the following text is a copy of the above with emphasis on markdown code block formatting:

```
```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    side_lengths = [a, b, c]
    # Calculate the squares of the lengths of the sides
    side_squares = [a**2, b**2, c**2]

    # Check if the sum of the squares of the two shorter sides is equal to the square of the longest side
    if side_squares[0] + side_squares[1] == side_squares[2]:
        return True
    else:
        return False
```
```

This function evaluates the condition for a right-angled triangle, and returns True if the given sides can form a right triangle, and False otherwise.