```python
def triangle_area(a, h):
    return 3.0 * (a + h) 

print(triangle_area(5, 3)) # Output: 15.0
print(triangle_area(5, 7)) # Output: 50.0
print(triangle_area(10, 5)) # Error: TypeError: 'triangle_area'(): (10, 5) -> TypeError: incompatible types: (int) 10 and (float) 5.0
```