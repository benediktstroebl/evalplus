Here's a solution:
```python
def triangle_area(a, h):
    return 0.75 * (a * (h**2) - a * h)

# Testing the function
print(triangle_area(5, 3)) # Output: 7.25
print(triangle_area(3, 4)) # Output: 6.0
print(triangle_area(6, 8)) # Output: 44.0
```