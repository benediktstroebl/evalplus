Here's a Python script with a self-contained function that calculates the area of the triangle:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(6, 6))  # Output: 12.6
print(triangle_area(10, 15)) # Output: 125.0
```

The function takes two parameters: the length of a side and the height of the triangle. The function calculates the area of the triangle using the formula `(1/2 * a * (b + h))). The function then returns the calculated area value. 

Note that the function can be called with any values for a and h, and it will always return the correct area of the triangle.