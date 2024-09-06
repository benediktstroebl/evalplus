Here's a self-contained Python function that calculates the area of a triangle based on its sides:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

#Test case 1:
assert triangle_area(5, 3) == 7.5

#Test case 2:
assert triangle_area(8, 6) == 34.8
```

This function takes two parameters, `a` and `h`, representing the lengths of the triangle's sides. It uses the mathematical formula to calculate the area of a triangle, `(a * (h + a) / 2)`, and returns the result.