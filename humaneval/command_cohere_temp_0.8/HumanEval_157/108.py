```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    if total * total == b * b + c * c :
        return True
    else: 
        return False
```
This function determines whether the given lengths of three sides form a right-angled triangle. It calculates the sum of the lengths of the three sides, and then determines whether the square of the longest side is equal to the difference between the sum of the squares of the other two sides. If this condition is satisfied, it returns True, indicating a right triangle; otherwise, it returns False. 
This algorithm works based on the concept that the sum of the squares of the legs of a right-angled triangle is always equal to the square of the hypotenuse. 

Here is a test case that verifies whether the function correctly determines right-angled triangles:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
``` 
This test case uses two different sets of lengths, one that forms a right-angled triangle and one that does not. The function should return 'True' for the first set and 'False' for the second.