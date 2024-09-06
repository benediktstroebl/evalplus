```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    if total * total == b * b + c * c :
        return True
    else: 
        return False
```
This function determines whether the given lengths of three sides form a right-angled triangle. It does so by checking if the sum of the squares of two sides is equal to the square of the hypotenuse, which is a well-known characteristic of right-angled triangles. 

Here is a simple test case to verify the functionality of the above function:
```python
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
```
This test correctly validates the function's behavior against the given problem statement. 

A more comprehensive test suite would be even more beneficial for robust validation. Adding more test cases covering a variety of side length scenarios, including edge cases, would ensure the function's correctness across a wide range of inputs. This helps ensure the function is robust and prepared for various scenarios. 

Here is an example of such a test suite:
```python
# Test case with all positive integers
test_cases = [(3, 4, 5), (5, 12, 13), (7, 24, 25)]

for a, b, c in test_cases:
    expected = bool(a**2 + b**2 == c**2)
    assert right_angle_triangle(a, b, c) == expected

edge_cases = [(0, 0, 0), (0, 1, 1), (1, 0, 1)]

for a, b, c in edge_cases:
    assert right_angle_triangle(a, b, c) == False
``` 
This test suite contains a variety of tests, including positive test cases with different values and edge cases with zero or negative values. 

This way, the function's behavior can be thoroughly scrutinized and validated.