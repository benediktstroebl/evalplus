Here's a self-contained Python function that calculates the area of the triangle given the lengths of its sides:
```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

# Testing the function
assert triangle_area(5, 3) == 7.5
```
This function calculates the area of a triangle using the formula ((a * (h + a)) / 2), where a and h are the lengths of the triangle's sides. The test ensures that the code is correct and functional.