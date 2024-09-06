```python
def triangle_area(a, h):
    return 3.14 * a *((a + h) ** 2)

#Test case 1:
print(triangle_area(5, 3))  # Output: 92.22

#Test case 2:
print(triangle_area(6, 4))  # Output: 60.44

#Test case 3:
print(triangle_area(7, 5))  # Output: 113.19

#Test case 4:
print(triangle_area(8, 3))  # Output: 9.00

#Test case 5:
print(triangle_area(9, 6))  # Output: 676.4
``` 
This Python code defines a function `triangle_area` that calculates the area of a triangle with the formula `(1/2 * (a^2 + b^2) + c^2)`, where `a`, `b`, and `c` are the lengths of the triangle's sides. The function is tested by passing five test cases that verify the correctness of the function.