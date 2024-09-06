```python
def triangle_area(a, h):
    return a * (h + a + h) / 2

print(triangle_area(5, 3)) # [5*4/2]= 20
print(triangle_area(5, 4)) # Error: (5*5)/2 is still 25, not 20.
```