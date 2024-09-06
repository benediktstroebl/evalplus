```python
def triangle_area(a, h):
    return (a * (h + a) ) / 2

# Test the function with invalid inputs (will fail)
triangle_area(5, 3)
triangle_area(-5, 3)
triangle_area(10, -3)

# Test the function with valid inputs
print(triangle_area(5, 3))
print(triangle_area(7, 8))

``` 
This Python code defines a function `triangle_area` that calculates the area of a triangle given the lengths of its sides. It tests this function with various sets of inputs and prints the results to the console.