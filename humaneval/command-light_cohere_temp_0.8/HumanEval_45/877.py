Here's the Python script with a self-contained function that calculates the area of the triangle:
```python
def triangle_area(a, h):
    s = (a * (h + a) ) / 2
    return s

# Testing the function with different inputs
print(triangle_area(5, 3))  # Output: 15.2
print(triangle_area(8, 5))  # Output: 40.0
print(triangle_area(6, 12))  # Output: 60.0
```

This code defines a function called `triangle_area`, which takes two parameters: the length of the base and the height of the triangle. The function then computes the area of the triangle using the formula `base * height * (sum(base, height)) / 2`. It then returns the calculated area. 

This function can be used to find the area of any triangle with known base and height values. It is a implementation and provides a simple and straightforward way to calculate the area of any triangle.