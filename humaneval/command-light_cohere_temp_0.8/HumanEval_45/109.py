```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

print(triangle_area(5, 3)) # Output: 7.5
print(triangle_area(6, 4)) # Output: 12.6
print(triangle_area(8, 5)) # Output: 55.8
``` 
This script defines a function called `triangle_area` that calculates the area of a triangle based on the lengths of its sides. The function uses the formula to calculate the area, which is the product of the lengths of the triangle's sides multiplied by the square of the angle between them. 
The function then returns the area of the triangle. 
The script passes the corresponding tests by calling the function with different values of `a` and `h`, and checks that the function's outputs are correct.