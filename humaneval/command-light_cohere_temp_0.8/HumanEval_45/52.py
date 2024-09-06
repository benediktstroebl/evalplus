Here's a self-contained Python function that calculates and returns the area of a triangle given its three sides:

```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # Semi-perimeter
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5
```

This function calculates the area using the formula for the area of a triangle and passes the test by providing any three side lengths and checking the result.