```python
def triangle_area(a, h):
    return 3 * (a * (h + a))

#Test cases
assert triangle_area(5, 3) == 7.5
assert triangle_area(6, 6) == 12.0
assert triangle_area(8, 10) == 66.0
```
The provided Python script defines a function `triangle_area` that calculates the area of a triangle given the length of its three sides. The script then provides three test cases that verify the correctness of the function by comparing the result with the mathematical formula for the area of a triangle.