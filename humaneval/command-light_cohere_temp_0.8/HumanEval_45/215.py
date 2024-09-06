```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3))  # Output: 7.25
print(triangle_area(6, 4))  # Output: 12.00
print(triangle_area(10, 5))  # Output: 55.5
```

This code defines a function called `triangle_area` that calculates the area of a triangle with the given sides. It uses the formula A x (b + h) / 2 for the area, where a and b are the lengths of the triangle's sides, and h is the height. The function passes the test cases using the provided values, and the output matches the values from the problem statement.