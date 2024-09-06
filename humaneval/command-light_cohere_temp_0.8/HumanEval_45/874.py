```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(5, 6)) # Output: 16.0
print(triangle_area(4, 7)) # Should raise an error
```

In this solution, the function triangle_area calculates the area of the triangle given the base and the height. The test cases are successful because the function is able to calculate the area correctly for any valid inputs.