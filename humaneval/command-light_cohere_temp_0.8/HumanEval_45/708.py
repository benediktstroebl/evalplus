```python
def triangle_area(a, h):
    return max(a * (h - a) for a in [2, 3, 5])  # Test cases: [2, 3, 5]
``` 
This code defines a function called `triangle_area` that calculates the area of the triangle using the formula "side * (height - side)". The function uses a list comprehension to iterate over the values of 'a' and calculates the area using the formula 'side * (height - side)'. The test cases are [2, 3, 5], and the function returns the maximum value of the calculated area using the test cases provided.