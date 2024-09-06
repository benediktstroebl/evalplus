```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

# Tests
print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(5, 4)) # Should raise an error
```
This function calculates the area of the triangle using Heron's formula, and tests its functionality with two input cases.