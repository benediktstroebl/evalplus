```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(6, 12)) # Output: 92.4
print(triangle_area(0.0, 10)) # Output: Error: ValueError: must provide length for sides

```