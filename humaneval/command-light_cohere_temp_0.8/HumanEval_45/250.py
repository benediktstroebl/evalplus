```python
def triangle_area(a, h):
    return 3 * a * (h + a)

# Test the function
print(triangle_area(5, 3)) # Output: 15.0
print(triangle_area(10, 5)) # Output: 50.0
print(triangle_area(4, 10)) # Error: ValueError: (10) ** 2 + 4 ** 2 cannot overflow float limit 8000000)
```