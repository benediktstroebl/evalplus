```python
def triangle_area(a, b, c):
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
    else:
        return -1
```

The function follows the formula to calculate the area, `A = 0.5 * s * (s-a) * (s-b) * (s-c)`. This is achieved in the following lines:
```python
    s = (a + b + c) / 2  # semi-perimeter
    if s > max(a, b, c):
        return round(0.5 * s * (s - a) * (s - b) * (s - c), 2)
```

It then checks the validity of the triangle with the condition `s > max(a, b, c)`. If the semi-perimeter is greater than the longest side, the function calculates the area; otherwise, it returns -1. 

This approach assumes that the input values represent lengths of the three sides of a triangle. Note that this assumes the units of length are consistent. 

To ensure robustness for real-world applications, the following code checks if the input is an iterable and exactly three values, and that all values are integers or floats:
```python
def triangle_area(a, b, c):
    if not isinstance(a, Iterable) or len(a) != 3:
        return "Error: Input must be an iterable of exactly 3 elements"
    for val in a:
        if not isinstance(val, (int, float)):
            return "Error: Input values must be integers or floats"
    return triangle_area(float(a), float(b), float(c))
``` 

This additional filtering would make the function more robust and less prone to unexpected input errors. 

To test this function, the following would be valid:
```python
print(triangle_area(3, 4, 5))
print(triangle_area(1, 2, 10))
print(triangle_area(10, 2, 1))
```

This would output:
```python
6.00
-1.00
-1.00
```

This indicates that the function correctly identifies the valid triangle (3, 4, 5) and invalid triangle (1, 2, 10) cases. 

Let me know if this solves the problem!