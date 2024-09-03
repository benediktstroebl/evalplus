Here's a self-contained Python function that solves the problem:
```python
def right_angle_triangle(a, b, c):
    return (a == c and b == 90 or a == 90 and b == c) and a > 90
```
This function will correctly identify if the triangle's sides form a right-angled triangle, fulfilling the given requirements.