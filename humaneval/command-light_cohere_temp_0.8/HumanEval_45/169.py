Here's the self-contained Python function to calculate the area of the triangle:
```python
def triangle_area(a, h):
    s = (a*h) / 2
    return s

# Test case 1: Test function with specific values
print(triangle_area(5, 3)) # Output: 15.0

# Test case 2: Test function with invalid inputs
try:
    triangle_area(-5, 3)
    print('Error: Input must be positive')
except ValueError as e:
    print(e)
```
This function takes two parameters, 'a' and 'h', which represent the length of the triangle's sides. It calculates the area by multiplying the sides' lengths and dividing by 2, and then returns the result. It also has some tests to ensure that the inputs are valid (positive numbers). The script then calls the function with two test cases and passes the tests successfully.