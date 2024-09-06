```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    return total * total == sq(a) + sq(b)

def sq(a):
    return a * a

# Test cases
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(1, 2, 3) == False
```

This script defines a function `right_angle_triangle` that determines whether the given lengths of three sides form a right-angled triangle. It does so by checking whether the sum of the lengths of the three sides squared is equal to the sum of the squares of any two of the sides.

The function `sq` is defined to square a given number. This is used to calculate the square of each side length, reducing complexity.

The test cases validate the behavior of the `right_angle_triangle` function with correct and incorrect input respectively.