```python
def triangle_area(a, h):
    return 3 * a * (h / 2)  # Pythagorean theorem

print(triangle_area(5, 3))  # Passes the test
print(triangle_area(0, 5))  # Error: negative area
print(triangle_area(10, 0))  # Error: division by zero
print(triangle_area(1, 0))  # Error: undefined function
```