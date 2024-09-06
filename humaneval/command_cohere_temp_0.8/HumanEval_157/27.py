```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    if total == 90 or total == 180:
        return True
    else:
        return False
```

The function `right_angle_triangle` returns true if the sum of the three lengths of the sides of the triangle is `90` or `180`, which defines the triangle as a right-angled triangle or not. It returns false otherwise. 

This algorithm has a time complexity of O(1) since it takes only a constant amount of time to check the conditions, regardless of the size of the input.