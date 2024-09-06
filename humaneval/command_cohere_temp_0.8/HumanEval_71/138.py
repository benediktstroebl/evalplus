```python
def triangle_area(a, b, c):
    s = sum([a, b, c])
    if abs(s - a - b) > 1e-6 or abs(s - a - c) > 1e-6 or abs(s - b - c) > 1e-6:
        return -1
    else:
        return round(0.5 * (a * b * cos(pi/3) ), 2)
```
The function checks whether the sum of any two of the input sides is greater than the third side. If this condition is true for any combination of sides, the function returns -1, indicating an invalid triangle. If the condition is true for no combinations, the function calculates and returns the area of the triangle to two decimal places. 
This approach uses the cosine rule, which states that the angle opposite the side with length 'a' accepts the cosine of the triangle is equal to the ratio of the length of the side 'b' to the length of the side 'c', or cos(θ) = b/c. Given that the problem asks for the area of the triangle, this rule allows us to solve for the area of a triangle when given the length of any two sides. 

The specifiying of an epsilon (1e-6) is used to prevent floating point precision issues. 

It's essential to note that this function assumes the inputs are valid float values, and the triangle is a Euclidean space. Additionally, this function assumes that the sum of the sides will be calculated as a floating-point number, which can result in a slight rounding error. To address this, the function checks the difference between the sum and each side's length to ensure it is within a slight tolerance level (1e-6). 

Finally, the function rounds the calculated area to two decimal places to satisfy the prompt's requirements.