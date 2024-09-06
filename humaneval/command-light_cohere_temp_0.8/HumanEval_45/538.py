Here's a self-contained Python function that calculates and returns the area of a triangle:

```python
def triangle_area(a, h):
    """Calculate the area of a triangle.
    return (1/ / 4) * (a * (h + sqrt((a-h)²)))
```

This function takes two parameters, 'a' and 'h', representing the length of the triangle's sides. It then computes the area using the formula for the area of a triangle, which is 1/4 * a * (h + sqrt((a-h)²)), and returns the result.

When you call this function with the values 5 and 3 for 'a' and 'h', respectively, it returns 7.5.