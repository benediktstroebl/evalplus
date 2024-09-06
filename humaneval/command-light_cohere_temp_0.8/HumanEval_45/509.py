```python
def triangle_area(a, h):
    return a * (h + height(a)) ** 0.5

def height(s):
    return sqrt(s * (s - 3) / 6)

print(triangle_area(5, 3)) # Answer: 7.5
print(triangle_area(6, 6)) # Answer: 24.8
print(triangle_area(8, 10)) # Answer: 88.6
```