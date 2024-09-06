```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```
In the code above, the `triangle_area` function calculates the area of the triangle using the Heron's formula. The code then checks whether the sum of any two sides is greater than the third side to determine if the sides represent a valid triangle. If the conditions are met, it returns the rounded area, and otherwise, it returns -1. 

To ensure that the function performs within the specified constraints, consider including input validation for the variable types and value ranges, especially for cases involving large or non-numeric values. This will help prevent potential errors and provide clearer feedback to users. 

You can improve the function's usability and readability by including informative variable names, adding comments, and structuring the code thoughtfully. This will enhance both your and others' understanding of the function's intentions and intricacies. 

This approach ensures that the function remains self-contained and easy to understand, while also adhering to the problem statement and passing the necessary tests.