```python
def triangle_area(a, h):
    return 3.0 * (a**/2) * (a + h)

print(triangle_area(5, 3)) # Output: 15.0
print(triangle_area(10, 5)) # Should raise an error
```

The function `triangle_area` takes two parameters, `a` and `h`, which represent the lengths of the sides of the triangle. The function then computes the area of the triangle using the formula for the area of a triangle, which is the product of the lengths of the three sides divided by 2.

The function then returns the computed area value.