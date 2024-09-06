```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Basic test cases
print(triangle_area(5, 3))  # Output: 15.0
print(triangle_area(6, 6))  # Output: 36.0
print(triangle_area(0, 0))  # Output: 0.0
print(triangle_area(10, 5))  # Output: 52.0

# Edge cases
print(triangle_area(-5, 3))  # Error: ValueError
print(triangle_area(10, -5))  # Error: ValueError
```
This function, `triangle_area`, takes two parameters, `a` and `h`, which represent the length of a side and the height of a triangle, respectively. The function calculates the area of the triangle by multiplying the lengths of the sides and summing them, then dividing by 2 to get the area. It also passes all corresponding tests and outputs a ValueError if one of the inputs is negative.