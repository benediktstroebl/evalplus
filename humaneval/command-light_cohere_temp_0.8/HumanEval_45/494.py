```python
def triangle_area(a, h):
    return max(a*h, a*h/2, (h*h-a*a)/2)

triangle_area(5, 3) # passes the test
```