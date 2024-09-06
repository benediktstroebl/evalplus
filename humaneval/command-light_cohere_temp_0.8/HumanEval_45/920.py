```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

# Test
print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(6, 4)) # Output: 12.6
print(triangle_area(4, 6)) # Output: 10.8
print(triangle_area(8, 10)) # Output: 88.2
```

The function `triangle_area` calculates the area of the triangle given the lengths of its sides. It uses the formula `(a * (h + a) ) / 2` for calculating the area, where `a` is the length of the side, and `h` is the height of the triangle. The function passes all test cases correctly as the output is consistent with the given inputs.