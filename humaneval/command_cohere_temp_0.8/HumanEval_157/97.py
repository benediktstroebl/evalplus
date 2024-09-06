```python
def right_angle_triangle(a, b, c):
    # Calculate the lengths of the sides of the triangle
    s = (a + b + c) / 2  #semi-perimeter of the triangle
    # Check if the triangle is a right-angled triangle
    if s*s == a*a + b*b or s*s == b*b + c*c or s*s == c*c + a*a:
        return True
    else: 
        return False
```

The function `right_angle_triangle` calculates the semi-perimeter of the triangle by summing the sides and dividing by 2. It then checks if the semi-perimeter squared equals the sum of two of the side lengths squared against the Pythagorean theorem, it returns True if they are equal, and False otherwise. It is worth noting that the order of the sides does not matter, as the function checks all possible combinations.