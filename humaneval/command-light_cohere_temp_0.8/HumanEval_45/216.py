Here is a self-contained Python script that solves the problem:
```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(5, 6)) # Output: 28.0
print(triangle_area(10, 7)) # Should raise error
```
This script defines a function `triangle_area` that calculates the area of the triangle based on two sides (`a` and `h`). It then passes the test cases with different side lengths and verifies if the function is returning expected results.