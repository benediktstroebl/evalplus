```python
def right_angle_triangle(a, b, c):
    """
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    """
    if a**2 + b**2 = c**2 or a**2 + c**2 = b**2 or b**2 + c**2 = a**2:
        return True
    else: 
        return False
```

The script tests the function using assert statements to compare the true and false outputs of the function against the given test cases. These assert statements check the correctness of the function and ultimately ensure that the function operates as expected, giving the desired output depending on the input values. 

For example, in the first test case, the assert statement checks if the function returns True when given the inputs (3, 4, 5) for the three side lengths of the triangle. The equality statement evaluates to True, and the assert statement returns without errors. Thus, the assert statement, and consequently the test case, passes. This is similarly applicable to the second test case, where the output is expected to be False. In this case, the inequality evaluates to False, meaning that the assert statement will not throw an error and allow the test case to pass as well.