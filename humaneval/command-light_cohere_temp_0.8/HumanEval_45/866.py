```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(5, 4)) # Output: 25.5
print(triangle_area(6, 3)) # Output: 30.25
print(triangle_area(6, 4)) # Output: 24.75
print(triangle_area(10, 15)) # Should fail due to overflow
```