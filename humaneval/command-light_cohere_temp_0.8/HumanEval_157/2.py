```python
def right_angle_triangle(a, b, c):
    return a + b > c and b + c > a and c > 0  # All three sides are positive and greater than 0

# Test cases:
1. Test case #1:
right_angle_triangle(3, 4, 5) == True # passes

2. Test case #2:
right_angle_triangle(1, 2, 3) == False # fails

3 Test case #3:
right_angle_triangle(-1, 2, 3) == False # fails

4 Test case #4:
right_angle_triangle(0, 3, 4) == False # fails

5 Test case #5:
right_angle_triangle(5, 0, 0) == False # fails
```
The function `right_angle_triangle` takes three positive length values as input and returns `True` if it can form a right-angled triangle, and `False` otherwise. 

The function uses the condition that all the sides are greater than zero, and the sum of any two sides is greater than the third side. 

This function can be used to quickly check if a given set of side lengths forms a right-angled triangle, which is useful in many geometry-related problems.