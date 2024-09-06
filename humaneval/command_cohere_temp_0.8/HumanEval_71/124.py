```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= max(a, b, c):
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)), 2)
    else:
        return -1
```

The function follows the formula for triangle area as explained, checks for the validity of the sides, and returns the area or -1 as stipulated in the prompt.

This approach handles both valid and invalid triangle scenarios, thus, checking for side validity is crucial to avoid potential division by zero errors. 

To ensure a balanced coverage of test scenarios, we should create tests for both valid and invalid triangles.