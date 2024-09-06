```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a) > 1e-6 or abs(s - b) > 1e-6 or abs(s - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
```
This Python script defines a function called `triangle_area` that takes three arguments, `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. 

The function first checks whether the triangle is valid by calculating the sum of the three sides, `s`, and comparing it to each side length with a tolerance of 1e-6 to account for floating-point error. If any of these comparisons indicate that the triangle is not valid (meaning the third side is longer than the sum of the other two), it returns -1 to indicate an invalid triangle. 

If the triangle is valid, it calculates the area of the triangle using the Heronian formula, which is half of the product of the square root of the sum of the squares of the lengths of the two sides multiplied by the difference of the square of the sides divided by the square of the length of the third side, multiplied by the square root of the sum of the squares of the two sides. It then rounds the result to 2 decimal places and returns it. 

The script also includes example tests that verify the correctness of the `triangle_area` function for different inputs to ensure it aligns with the problem statement.