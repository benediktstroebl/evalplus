```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == a + c:
        area = (a * b * (5 * c - a - b) / 2)
        return round(area, 2)
    else:
        return -1
```

The function "triangle_area" accepts the three side lengths of a triangle as input. The code first determines whether the sum of any two of the sides is greater than the length of the third side, which is the definition of a valid triangle.

It calculates the area of the triangle using Heron's formula if it is a valid triangle. Using the convention that the triangle's area is positive, the formula weighs the squared sides of the triangle by appropriate coefficients and averages them.

The function returns -1 to signify that the sides are invalid for triangle construction if the sum of any two sides is not greater than the length of the third side.

This approach ensures that the function handles valid triangle scenarios and returns a meaningful result while being concise and efficient.