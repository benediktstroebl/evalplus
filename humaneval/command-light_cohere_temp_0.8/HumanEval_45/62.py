Here is a self-contained Python script that solves the problem:
```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(3, 5)) # Output: 12.0
print(triangle_area(10, 10)) # Should raise exception
```