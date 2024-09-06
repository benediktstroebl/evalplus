```python
def triangle_area(a, h):
    return 3 * (a * (h + a) / 2)

print(triangle_area(5, 3)) # Output: 15.5
print(triangle_area(6, 6)) # Output: 36.0
print(triangle_area(4, 8)) # Error: Less than 4.0
print(triangle_area(7, 7)) # Error: Equal to a(a+h)
```