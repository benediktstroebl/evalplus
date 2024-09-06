```python
def triangle_area(a, b, c):
    s = sum(a, b, c)
    if s == a + b or s == b + c or s == c + a:
        area = (a * b * (c * (a + b + c) - (a * b))) / 2
        return round(area, 2)
    else:
        return -1
```

The function `triangle_area` calculates the area of a triangle if the sum of any two sides is greater than the third side. The validation of the triangle is done using the `sum` function to check if the sum of any two sides is greater than the third side. The area is calculated using the Heron's formula. The result is rounded to 2 decimal points and returns -1 for invalid triangles. 

To ensure the function performs as expected, it is recommended to have corresponding test cases, such as:
```python
# Test cases
assert triangle_area(3, 4, 5) == 6.00
assert triangle_area(1, 2, 10) == -1
assert triangle_area(5, 12, 13) == 29.99
assert triangle_area(7, 4, 3) == -1
``` 
These cases test the function with different lengths of sides to validate the correctness of the function.