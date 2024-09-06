```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Test case 1
assert triangle_area(5, 3) == 7.5

# Test case 2
assert triangle_area(10, 5) == 50

# Test case 3
try:
    print(triangle_area(-5, -3))
except Exception as e:
    print(e)
```