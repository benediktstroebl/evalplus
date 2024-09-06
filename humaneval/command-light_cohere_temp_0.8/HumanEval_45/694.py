```python
def triangle_area(a, h):
    return 3.14 * a * (a**2 + h*h)

print(triangle_area(5, 3)) # Output: 28.28
print(triangle_area(10, 5)) # Error: ValueError
 ```