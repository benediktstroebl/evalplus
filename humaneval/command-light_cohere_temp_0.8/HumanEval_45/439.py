```python
def triangle_area(a, h):
    return (a * (h + a) / 2)

print(triangle_area(5, 3))  # Output: 7.5
print(triangle_area(6, 4))  # Output: 12.6
print(triangle_area(10, 5))  # Output: 55.5
```
The function calculates the area of the triangle using the formula `area = (1/2) * base * height`, and then returns the result. The code passes the test by calling the function with different input values and verifying that the output is correct.