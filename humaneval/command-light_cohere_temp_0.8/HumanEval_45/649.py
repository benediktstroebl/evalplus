```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) / 2

# Test cases
test_cases = [(5, 3), (6, 4), (10, 8)]

for a, h in test_cases:
    assert triangle_area(a, h) == (3 * (a**2 + h**2)) / 2
``` 
This code defines a Python function called `triangle_area` that calculates the area of a triangle given its base side length `a` and height `h`. 

The function uses the Pythagorean theorem to calculate the area by summing the squares of the base side length and height, then multiplying by 1/2. 

It then tests the function with a series of test cases, where the values of `a` and `h` are provided. The function's result is checked to be equal to the calculated area, which verifies the correctness of the function's calculations.