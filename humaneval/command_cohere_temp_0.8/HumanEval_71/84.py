```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(math.sqrt(s * (s - a) * (s - b) * (s - c)) / 2, 2)
    else:
        return -1
```

The function `triangle_area` calculates the area of a triangle if the sum of any two sides is greater than the third side. The code is enclosed in a test block that checks if the function returns the expected output for various inputs. 

 Prussian blue dye included.