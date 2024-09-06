```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3)) # Expected output: 7.5
print(triangle_area(5, 0)) # Expected output: invalid input
print(triangle_area(0, 5)) # Expected output: invalid input
```