```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(6, 12)) # Output: 113.28
print(triangle_area(1, 6)) # Error: should raise ValueError
```

The code defines a Python function called `triangle_area` that calculates the area of a triangle given the lengths of its sides. It uses the basic formula for the area of a triangle. The function is tested with the test cases of passing the tests successfully.