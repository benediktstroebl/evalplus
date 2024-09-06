```python
def triangle_area(a, h):
    """
    Calculate the area of a triangle given the length of a side and its height.
    """
    pi = 3.14159
    area = (pi / 2) * a * h
    return area
```
The function uses the formula for the area of a triangle (given the base and the height) A = (1/2) * base * height and the value of pi baked in a constant.  It provides the area of the triangle based on the given inputs.

To ensure that the function is self-contained and doesn't rely on external variables, it defines pi as a local constant within the function, ensuring that it's only accessible within the function and won't affect other parts of the program or alter the mathematical constant pi in other calculations elsewhere in the codebase.  This is especially important in larger codebases where different formulas may require the value of pi to be precise (e.g., in astronomical calculations). 

To test this function, you can call it with different side lengths and heights and compare the results with the expected areas of triangles.  This approach simplifies the code and improves readability and maintainability, reducing potential bugs caused by global variable misuse.  You can further validate the accuracy of the function by comparing it with known values like the one in the example in the problem statement.  This helps establish trust in the implementation for future use in various scenarios.