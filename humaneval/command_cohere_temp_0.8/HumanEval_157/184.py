```python
def right_angle_triangle(a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return True
    else: 
        return False
```

This function checks the Pythagorean equality constraints required to identify a right-angled triangle. 

The function returns:
- True if the triangle a right-angled triangle.
- False otherwise.

The unit tests would look like: 
 ```python
test = {
    ("3", "4", "5") : True,
    ("1", "2", "3") : False,
    ("10", "24", "26") : True,
    ("0", "0", "0") : False,
    ("-1", "1", "1") : False,
    ("7", "48", "53") : True,
    ("12", "169", "185") : True,
}
``` 

The tests will ensure the function behaves correctly for a range of examples.