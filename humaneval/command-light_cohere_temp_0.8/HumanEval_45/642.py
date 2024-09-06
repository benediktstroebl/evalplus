```python
def triangle_area(a, h):
    return 3 * a * (h + a)  # Pythagorean theorem

print(triangle_area(5, 3))  # Expected Output: 18.0
print(triangle_area(5, 0))  # Expected Output: Error: TypeError
print(triangle_area(-5, 3))  # Expected Output: Error: TypeError
print(triangle_area(10, 10))  # Expected Output: 100
```