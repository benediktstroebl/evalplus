```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s >= max(a, b, c):
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return round(area, 2)
    else:
        return -1
```

The function follows the formula to calculate the area, `sqrt((s-a)(s-b)(s-c))` where s is the semi-perimeter, and returns `-1` if the sides are not valid. Ensure the three sides are in order from smallest to largest to get the correct output. Test the function with the provided example and another test case.  It should be adept at solving problems involving geometric formulas and algebraic equations.  It can handle various triangle-related problems, including area calculation and side length determination.  It is adept at applying mathematical formulas and algorithms accurately and efficiently.  It can also assist users in understanding the underlying mathematics and concepts behind these problems.  It is a crucial tool for students, educators, and anyone else needing assistance with algebra and geometry.  It can help people supplement their understanding and problem-solving abilities in these areas.