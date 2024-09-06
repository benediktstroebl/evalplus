```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```
The above `right_angle_triangle()` function can efficiently determine whether the three sides of a given triangle form a right-angled triangle. It does so by checking if any of the three possible combinations of the squared side lengths equal the squared hypotenuse length, which is a well-known characteristic of right-angled triangles. 

This approach ensures the correct identification of right-angled triangles with a time complexity of O(1), making it a highly optimized solution.

Here is a sample implementation of test cases to ensure the correctness of the implementation:
```python
# Testing a valid case
print(right_angle_triangle(3, 4, 5))  # Should print True

# Testing invalid cases
print(right_angle_triangle(1, 2, 3))   # Should print False
print(right_angle_triangle(7, 8, 9))   # Should print False
print(right_angle_triangle(10, 10, 1)) # Should print False
```
This would test the function with true and false cases, ensuring that it behaves as intended.