```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```
In the script, the function `triangle_area` takes in three parameters `a`, `b`, and `c`, representing the lengths of the three sides of a triangle. It calculates the semi-perimeter `s`, which is half of the sum of the three sides. The condition `s > max(a, b, c)` checks if the semi-perimeter is greater than the longest side of the triangle. If this condition is met, the function calculates the area of the triangle using the formula `0.5 * s * (s - a) * (s - b) * (s - c)`, with the correct denominator, and rounds it to two decimal places. If the condition is not met, it returns `-1` to indicate that the sides do not form a valid triangle. 

To help understand the logic behind the approach, here's an outline of the steps involved in solving the problem:
1. Determine the semi-perimeter `s`: The semi-perimeter s of a triangle is given by the average of the sum of any two sides with the third side. In other words, `s = (a + b + c) / 2`. This value represents the average length of the sides of the triangle.
2. Verify if the sides form a valid triangle: To check if the given sides form a valid triangle, use the criterion that the sum of any two sides should be greater than the third side. In terms of the semi-perimeter, this translates to checking if `s > max(a, b, c)`.
3. If valid, calculate the area: If the semi-perimeter `s` is greater than the largest side, it means the sides satisfy the triangle inequality. To calculate the area of the triangle in this case, use the formula `Area = 0.5 * s * (s - a) * (s - b) * (s - c)`. This formula derives from the fact that the area of a triangle is proportional to the product of its sides' lengths, with the constant of proportionality being 0.5.
4. If not valid, return an error message: If the semi-perimeter is less than or equal to the largest side, it means the sides do not form a valid triangle. In this case, return an appropriate error message or a value like `-1` to signify an invalid triangle.

This problem highlights the importance of understanding the concepts of triangles and their properties, as well as applying mathematical formulas accurately to calculate the area. It is essential to carefully analyze the problem and apply the appropriate steps to obtain the correct solution.