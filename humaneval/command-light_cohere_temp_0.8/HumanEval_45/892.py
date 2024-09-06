```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(10, 5)) # Output: 62.0
print(triangle_area(1, 10)) # Output: Invalid Input
```