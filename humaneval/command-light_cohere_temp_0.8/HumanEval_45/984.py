```python
def triangle_area(a, h):
    return (a * (h + a) / 2) ** .5

print(triangle_area(5, 3)) #Should print 7.5
print(triangle_area(6, 4)) #Should print 12.0
print(triangle_area(4, 6)) #Should print 10.0
print(triangle_area(8, 10)) #Should print 69.0
```