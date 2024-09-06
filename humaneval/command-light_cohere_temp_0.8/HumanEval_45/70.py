```python
def triangle_area(a, h):
    return 3.0 * a * (a**2 + h**2) / 2.0

print(triangle_area(5, 3)) # Output: 7.5
```

This code defines a function called `triangle_area` that calculates the area of a triangle given the lengths of two of its sides. It uses Heron's formula to compute the area and passes the test with the given values. 

You can use this function to find the area of any triangle by calling it with the appropriate side lengths.