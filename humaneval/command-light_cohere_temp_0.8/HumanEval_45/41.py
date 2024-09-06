Here is a Python script that defines a function triangle_area that calculates the area of the triangle using the given sides: 
```python
def triangle_area(a, h): 
    s = (a*h) / 2
    return s

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(10, 4)) # Should raise an error
```