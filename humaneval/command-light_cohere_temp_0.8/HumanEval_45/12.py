```python
def triangle_area(a, h):
    return 3 * (a**2 + h**2) ** (1/2)

# Test drive function
print(triangle_area(5, 3))  # Output: 45
print(triangle_area(0, 5))  # Error: ValueError
print(triangle_area(3, 0))  # Error: ValueError
print(triangle_area(-5, 3))  # Error: ValueError
```