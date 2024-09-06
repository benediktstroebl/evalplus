```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3)) # prints: 15.5
print(triangle_area(5, 6)) # prints: 30.0
print(triangle_area(6, 5)) # fails, throws TypeError
```