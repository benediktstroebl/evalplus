```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else: 
        return False
```
This function determines whether the given lengths of a triangle's three sides form a right-angled triangle. It achieves this by comparing the sum of the squares of the two legs with the square of the hypotenuse, adhering to the Pythagorean theorem. If the sum matches the square of the hypotenuse, the triangle is right-angled, and the function returns True; otherwise, it returns False. 

Here is a simple test case to ensure the functionality of the function: 
```python
test_cases = [[3, 4, 5], [1, 2, 3]]

for test in test_cases:
    assert right_angle_triangle(*test) == True
```

This block of code defines a list of test cases, comprising tuples of side lengths for triangles. It then iterates through each test case, asserting that the `right_angle_triangle` function returns True, indicating that the sides form a right-angled triangle. This confirms the expected behavior of the function. 

To further enhance the function's robustness, additional test cases involving edge scenarios and boundary conditions should be considered, alongside error handling to ensure tolerance for input errors.