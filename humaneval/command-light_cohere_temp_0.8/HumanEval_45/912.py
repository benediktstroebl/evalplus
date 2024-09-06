```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(6, 6)) # Output: 12.0
print(triangle_area(10, 5)) # Error: 10**2 /2 is not a triangle
```
The error is due to the fact that the area of a triangle is the product of the base and height divided by 2, not the sum.