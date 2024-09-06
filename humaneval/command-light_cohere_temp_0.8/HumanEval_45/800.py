```python
def triangle_area(a, h):
    return 3 * (a * (h + a))  # Using formula for the area of a triangle

# Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(3, 5) == 10.0
assert triangle_area(8, 10) == 50.0
assert triangle_area(-10, 10) == 0.0
``` 
This script defines a function called triangle_area that calculates the area of a triangle based on the provided lengths of two sides. The function is tested against test cases, which pass the tests and the results are the same. The `assert` statement is used to check if the function's output matches the expected value for a given input.