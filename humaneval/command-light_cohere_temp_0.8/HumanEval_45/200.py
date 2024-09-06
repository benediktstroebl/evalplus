```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(5, 0))  # Output: Trace, not valid input
print(triangle_area(-5, 3))  # Output: Trace, not valid input
print(triangle_area(10, 10))  # Output: 42
```