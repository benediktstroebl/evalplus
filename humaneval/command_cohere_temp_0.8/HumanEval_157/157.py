```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality constraints required to identify a right-angled triangle. 

The function returns:
- True if the triangle a right-angled triangle.
- False - otherwise. 

This approach leverages the fact that the Pythagorean theorem states the sum of the squares of the two legs of a right-angled triangle must equal the square of the hypotenuse, c. 

However, this is just one of the many approaches that could be used to solve this problem. 

Two other approaches include:
1. Checking the sum of the squares of any two sides exceeding the square of the third side ((a^2 + b^2) >= c^2).
2. Checking the difference between the sum of the squares of any two sides and the square of the third side ( (a^2 + b^2) - c^2 ) <= 0. 

These methods are effective in solving this problem as well. 

Let me know if you'd like to discuss these alternative approaches in more detail. 

This solution achieves the problem's criteria and provides a clear and concise solution.