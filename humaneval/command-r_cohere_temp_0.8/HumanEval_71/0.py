```python
def triangle_area(a, b, c):
    '''
    Calculates the area of a triangle given its three sides. 
    Returns the area rounded to 2 decimal places if the sides form a valid triangle, 
    else returns -1.
    '''
    # Check if the triangle is valid
    if a + b > c and a + c > b and b + c > a:
        area = (a + b + c) / 4
        return round(area, 2)
    else:
        return -1
```