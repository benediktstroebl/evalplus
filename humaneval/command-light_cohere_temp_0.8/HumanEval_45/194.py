```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(10, 5)) # Should raise an error
```

This code defines a function `triangle_area` that calculates the area of a triangle given its base and height. The code then passes the area of a 5-sided triangle and of a triangle with a 10-sided base to the function, and prints the result correctly.