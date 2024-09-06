```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if abs(s - max(s)) < 1e-5:
        return round(0.5 * (a * b * sin(π/3)) / (a + b + c), 2)
    else:
        return -1
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first calculates the sum of the three side lengths, `s = sum(a, b, c)`. It then checks if the difference between the sum and the longest side is close to zero (`abs(s - max(s)) < 1e-5`) to determine if the three sides form a valid triangle. If the condition is met, it calculates the area of the triangle using the formula `0.5 * (a * b * sin(π/3)) / (a + b + c)`. This formula is based on the fact that the triangle is equilateral, and the area of an equilateral triangle is half of its side length multiplied by the sine of its angle. The result is then rounded to two decimal places and returned. 

If the sides do not form a valid triangle, meaning that the sum of any two sides is not greater than the third side, the function returns -1. 

This script provides a clean and efficient way to determine the area of a triangle given its side lengths, while also ensuring the validity of the inputs.